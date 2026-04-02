FROM nginx:alpine
# 기존 nginx 웹 서버 사용
COPY app/ /usr/share/nginx/html/
# 나의 app 디렉토리를 nginx 기본 페이지 위치로 복사