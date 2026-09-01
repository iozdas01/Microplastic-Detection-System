#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
compose_file="${repo_dir}/infra/firecrawl/docker-compose.yml"
firecrawl_url="${FIRECRAWL_BASE_URL:-http://127.0.0.1:3002}"

compose() {
  docker-compose -f "${compose_file}" "$@"
}

case "${1:-status}" in
  up)
    if ! colima status >/dev/null 2>&1; then
      colima start --cpu 4 --memory 6 --disk 60 --vm-type vz
    fi
    compose up -d
    ;;
  down)
    compose down
    ;;
  status)
    colima status
    compose ps
    curl --fail --silent --show-error --max-time 5 \
      "${firecrawl_url}/" >/dev/null
    echo "Firecrawl reachable at ${firecrawl_url}"
    ;;
  logs)
    compose logs --tail=200 "${2:-api}"
    ;;
  smoke-test)
    curl --fail --silent --show-error --max-time 90 \
      -H "Content-Type: application/json" \
      -d '{"query":"manual workflow workaround","limit":1,"sources":["web"],"includeDomains":["reddit.com"],"timeout":90000,"scrapeOptions":{"formats":["markdown"],"onlyMainContent":true}}' \
      "${firecrawl_url}/v2/search" |
      python3 -c 'import json,sys; p=json.load(sys.stdin); rows=(p.get("data") or {}).get("web", []); assert p.get("success") and rows and "reddit.com" in rows[0].get("url", ""), "no Reddit result"; print(json.dumps({"success": True, "url": rows[0]["url"], "title": rows[0].get("title", ""), "markdown_chars": len(rows[0].get("markdown", ""))}, indent=2))'
    ;;
  *)
    echo "Usage: $0 {up|down|status|logs [service]|smoke-test}" >&2
    exit 2
    ;;
esac
