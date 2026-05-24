#!/bin/bash
# 관상감 데모 서버 시작 스크립트
# 더블클릭하면 자동으로 서버 시작 + 브라우저 열림

cd "$(dirname "$0")"

# Find available port
PORT=8000
while lsof -ti:$PORT > /dev/null 2>&1; do
  PORT=$((PORT + 1))
done

echo "════════════════════════════════════════"
echo "  관상감 데모 서버 시작"
echo "  Port: $PORT"
echo "════════════════════════════════════════"
echo ""
echo "  접속 URL:"
echo "  → http://localhost:$PORT/index.html"
echo "  → http://localhost:$PORT/demo-delta-bruno-v3.html  ⭐ 추천"
echo ""
echo "  종료: 이 창에서 Ctrl+C"
echo "════════════════════════════════════════"

# Open browser after 1.5s
(sleep 1.5 && open "http://localhost:$PORT/demo-delta-bruno-v3.html") &

# Start Python HTTP server
python3 -m http.server $PORT
