const OWNER = process.env.GITHUB_OWNER || "iozdas01";
const REPO = process.env.GITHUB_REPO || "Microplastic-Detection-System";
const BRANCH = process.env.GITHUB_BRANCH || "main";
const DATA_PATH = "data/kanban.json";
const MAX_ACTIVITY = 100;

function githubHeaders() {
  const headers = {
    Accept: "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "microplastic-control-room",
  };
  if (process.env.GITHUB_TOKEN) {
    headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
  }
  return headers;
}

function send(res, status, body) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.end(JSON.stringify(body));
}

function cleanText(value, max) {
  return String(value || "").replace(/[\u0000-\u001f]/g, " ").trim().slice(0, max);
}

async function readBoard() {
  const url = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${DATA_PATH}?ref=${encodeURIComponent(BRANCH)}`;
  const response = await fetch(url, { headers: githubHeaders() });
  if (!response.ok) throw new Error(`GitHub read failed (${response.status})`);
  const file = await response.json();
  const json = Buffer.from(file.content.replace(/\n/g, ""), "base64").toString("utf8");
  return { board: JSON.parse(json), sha: file.sha };
}

function addActivity(board, type, task, from, to) {
  board.activity = Array.isArray(board.activity) ? board.activity : [];
  board.activity.unshift({
    id: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
    at: new Date().toISOString(),
    type,
    task_id: task.id,
    title: task.title,
    from: from || null,
    to: to || task.status,
  });
  board.activity = board.activity.slice(0, MAX_ACTIVITY);
}

function applyAction(board, payload) {
  board.tasks = Array.isArray(board.tasks) ? board.tasks : [];
  const allowedStatuses = ["backlog", "next", "doing", "done"];
  const action = cleanText(payload.action, 20);

  if (action === "create") {
    const title = cleanText(payload.title, 140);
    if (!title) throw new Error("A task title is required");
    const status = allowedStatuses.includes(payload.status) ? payload.status : "backlog";
    const task = {
      id: `T-${Date.now().toString(36).toUpperCase()}-${Math.random().toString(36).slice(2, 6).toUpperCase()}`,
      title,
      detail: cleanText(payload.detail, 600),
      priority: ["high", "normal", "low"].includes(payload.priority) ? payload.priority : "normal",
      status,
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString(),
    };
    board.tasks.push(task);
    addActivity(board, "created", task, null, status);
    return { board, task, message: `board: add ${title}` };
  }

  const task = board.tasks.find((item) => item.id === payload.id);
  if (!task) throw new Error("Task not found");

  if (action === "move") {
    if (!allowedStatuses.includes(payload.status)) throw new Error("Invalid task status");
    const from = task.status;
    task.status = payload.status;
    task.updated_at = new Date().toISOString();
    addActivity(board, "moved", task, from, task.status);
    return { board, task, message: `board: move ${task.title} to ${task.status}` };
  }

  if (action === "update") {
    const previousTitle = task.title;
    const title = cleanText(payload.title, 140);
    if (!title) throw new Error("A task title is required");
    task.title = title;
    task.detail = cleanText(payload.detail, 600);
    task.priority = ["high", "normal", "low"].includes(payload.priority) ? payload.priority : task.priority;
    task.updated_at = new Date().toISOString();
    addActivity(board, "updated", task, null, task.status);
    return { board, task, message: `board: update ${previousTitle}` };
  }

  if (action === "delete") {
    board.tasks = board.tasks.filter((item) => item.id !== task.id);
    addActivity(board, "deleted", task, task.status, null);
    return { board, task, message: `board: remove ${task.title}` };
  }

  throw new Error("Unsupported action");
}

async function writeBoard(board, sha, message) {
  if (!process.env.GITHUB_TOKEN) throw new Error("GITHUB_TOKEN is not configured");
  const url = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${DATA_PATH}`;
  board.updated_at = new Date().toISOString();
  const response = await fetch(url, {
    method: "PUT",
    headers: { ...githubHeaders(), "Content-Type": "application/json" },
    body: JSON.stringify({
      message: message.slice(0, 120),
      content: Buffer.from(`${JSON.stringify(board, null, 2)}\n`, "utf8").toString("base64"),
      sha,
      branch: BRANCH,
    }),
  });
  if (!response.ok) {
    const error = await response.text();
    throw new Error(`GitHub write failed (${response.status}): ${error.slice(0, 180)}`);
  }
  return response.json();
}

module.exports = async function handler(req, res) {
  if (req.method !== "GET" && req.method !== "POST") {
    res.setHeader("Allow", "GET, POST");
    return send(res, 405, { error: "Method not allowed" });
  }

  try {
    const { board, sha } = await readBoard();
    if (req.method === "GET") return send(res, 200, board);

    if (!process.env.BOARD_WRITE_KEY) {
      return send(res, 503, { error: "BOARD_WRITE_KEY is not configured" });
    }
    if (req.headers["x-board-key"] !== process.env.BOARD_WRITE_KEY) {
      return send(res, 401, { error: "The board write key is missing or incorrect" });
    }

    const payload = typeof req.body === "string" ? JSON.parse(req.body) : (req.body || {});
    const result = applyAction(board, payload);
    await writeBoard(result.board, sha, result.message);
    return send(res, 200, { board: result.board, task: result.task });
  } catch (error) {
    const status = /required|not found|invalid|unsupported/i.test(error.message) ? 400 : 500;
    return send(res, status, { error: error.message });
  }
};
