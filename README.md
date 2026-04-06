## 1. 프로젝트 개요(미션 목표 요약)

## 2. 실행 환경(OS/쉘/터미널, Docker버전, Git버전)

- OS :
- Shell : GNU bash, version 3.2.57(1)-release (x86_64-apple-darwin24)
- Docker : Docker version 28.5.2, build ecc6942
- Git : git version 2.53.0

## 3. 수행 항목 체크리스트

### 3-1. 터미널 기본 조작 및 폴더 구성

- 절대 경로 vs 상대 경로
    - 절대 경로
        - 루트(/)부터 시작하는 전체 경로
    - 상대 경로
        - 현재 위치를 기준으로 계산하는 경로
- 현재 위치 확인, 목록 확인(숨김 파일 포함), 이동, 생성, 복사, 이동/이름변경, 삭제

```jsx
//현재 위치 확인
jeay5290857@c3r4s3 ~ % pwd
/Users/jeay5290857

//목록 확인(숨김 파일 포함)
jeay5290857@c3r4s3 ~ % ls -a
.			.ssh			Library
..			.vscode			Movies
.CFUserTextEncoding	.zsh_history		Music
.DS_Store		.zsh_sessions		OrbStack
.Trash			Codyssey		Pictures
.copilot		Desktop			Public
.docker			Documents
.orbstack		Downloads

//디렉토리 생성
jeay5290857@c3r4s3 ~ % mkdir test   
jeay5290857@c3r4s3 ~ % ls -a
.			.ssh			Library
..			.vscode			Movies
.CFUserTextEncoding	.zsh_history		Music
.DS_Store		.zsh_sessions		OrbStack
.Trash			Codyssey		Pictures
.copilot		Desktop			Public
.docker			Documents		test
.orbstack		Downloads

//파일 생성
jeay5290857@c3r4s3 ~ % vi test.txt
jeay5290857@c3r4s3 ~ % ls
Codyssey	Downloads	Music		Public
Desktop		Library		OrbStack	test
Documents	Movies		Pictures	test.txt

//파일 이동
jeay5290857@c3r4s3 ~ % mv test.txt ~/test
jeay5290857@c3r4s3 ~ % ls
Codyssey	Downloads	Music		Public
Desktop		Library		OrbStack	test
Documents	Movies		Pictures
jeay5290857@c3r4s3 ~ % cd test && ls
test.txt

//파일 복사
jeay5290857@c3r4s3 test % cp test.txt ~      
jeay5290857@c3r4s3 test % ls
test.txt
jeay5290857@c3r4s3 test % cd .. && ls
Codyssey	Downloads	Music		Public
Desktop		Library		OrbStack	test
Documents	Movies		Pictures	test.txt

//파일 이동/이름변경
jeay5290857@c3r4s3 ~ % mv test.txt ~/test/test1.txt
jeay5290857@c3r4s3 ~ % ls
Codyssey	Downloads	Music		Public
Desktop		Library		OrbStack	test
Documents	Movies		Pictures
jeay5290857@c3r4s3 ~ % cd test
jeay5290857@c3r4s3 test % ls
test.txt	test1.txt

//파일/디렉토리 삭제
jeay5290857@c3r4s3 ~ % ls
Codyssey	Downloads	Music		Public
Desktop		Library		OrbStack	test
Documents	Movies		Pictures
jeay5290857@c3r4s3 ~ % rm -rf test
jeay5290857@c3r4s3 ~ % ls
Codyssey	Documents	Library		Music		Pictures
Desktop		Downloads	Movies		OrbStack	Public

```

- 파일 내용 확인, 빈 파일 생성

```jsx
//빈 파일 생성
jeay5290857@c3r4s3 test % touch a.txt
jeay5290857@c3r4s3 test % ls
a.txt

//파일 내용 확인
jeay5290857@c3r4s3 test % cat a.txt
jeay5290857@c3r4s3 test % 
```

### 3-2. 권한 변경 실습

- 권한
    - d || - : 디렉토리 || 파일
    - r : read, w : write, x : execute
    - o : 소유자, g : 그룹, o : 기타
- 권한을 확인/변경하는 명령을 수행하고, 변경 전/후 비교를 기술 문서에 남긴다.

```jsx
jeay5290857@c3r4s3 test % ls -l
total 0
drwxr-xr-x  2 jeay5290857  jeay5290857  64 Mar 30 20:11 a
-rw-r--r--  1 jeay5290857  jeay5290857   0 Mar 30 20:06 a.txt
```

- 최소 요구: 파일 1개, 디렉토리 1개에 대해 권한 변경 실험을 수행한다.

```jsx
//파일 권한 변경
jeay5290857@c3r4s3 test % chmod 777 a.txt
jeay5290857@c3r4s3 test % ls -l
total 0
drwxr-xr-x  2 jeay5290857  jeay5290857  64 Mar 30 20:11 a
-rwxrwxrwx  1 jeay5290857  jeay5290857   0 Mar 30 20:06 a.txt

//디렉토리 권한 변경
jeay5290857@c3r4s3 test % chmod 777 a
jeay5290857@c3r4s3 test % ls -l
total 0
drwxrwxrwx  2 jeay5290857  jeay5290857  64 Mar 30 20:11 a
-rwxrwxrwx  1 jeay5290857  jeay5290857   0 Mar 30 20:06 a.txt
```

### 3-3. Docker 설치/점검

- docker 버전 확인

```jsx
jeay5290857@c3r4s3 test % docker --version
Docker version 28.5.2, build ecc6942
```

- docker 데몬 동작 여부 확인
    
    docker info 명령을 통해 Docker Client와 Server 정보를 확인하였다.
    Server 항목이 출력되어 Docker 데몬이 정상 동작 중임을 확인할 수 있었다.
    또한 Context가 orbstack으로 표시되어 OrbStack이 Docker 실행 환경을 제공하고 있음을 확인하였다.
    Operating System은 OrbStack, OSType은 linux로 표시되어 내부적으로 Linux 기반 컨테이너 환경이 동작함을 알 수 있었다.
    

```jsx
jeay5290857@c3r4s3 test % docker info
Client:
 Version:    28.5.2
 Context:    orbstack           //orbstack 이용중
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/jeay5290857/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/jeay5290857/.docker/cli-plugins/docker-compose

Server:                        //docker demon 정상 작동
 Containers: 3
  Running: 1
  Paused: 0
  Stopped: 2
 Images: 3
 Server Version: 28.5.2
 Storage Driver: overlay2
  Backing Filesystem: btrfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 1c4457e00facac03ce1d75f7b6777a7a851e5c41
 runc version: d842d7719497cc3b774fd71620278ac9e17710e0
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.17.8-orbstack-00308-g8f9c941121b1
 Operating System: OrbStack
 OSType: linux                            //OS type 리눅스
 Architecture: x86_64
 CPUs: 6
 Total Memory: 15.67GiB
 Name: orbstack
 ID: 0d6f71cb-340e-4735-9a61-68acf17b02aa
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Product License: Community Engine
 Default Address Pools:
   Base: 192.168.97.0/24, Size: 24
   Base: 192.168.107.0/24, Size: 24
   Base: 192.168.117.0/24, Size: 24
   Base: 192.168.147.0/24, Size: 24
   Base: 192.168.148.0/24, Size: 24
   Base: 192.168.155.0/24, Size: 24
   Base: 192.168.156.0/24, Size: 24
   Base: 192.168.158.0/24, Size: 24
   Base: 192.168.163.0/24, Size: 24
   Base: 192.168.164.0/24, Size: 24
   Base: 192.168.165.0/24, Size: 24
   Base: 192.168.166.0/24, Size: 24
   Base: 192.168.167.0/24, Size: 24
   Base: 192.168.171.0/24, Size: 24
   Base: 192.168.172.0/24, Size: 24
   Base: 192.168.181.0/24, Size: 24
   Base: 192.168.183.0/24, Size: 24
   Base: 192.168.186.0/24, Size: 24
   Base: 192.168.207.0/24, Size: 24
   Base: 192.168.214.0/24, Size: 24
   Base: 192.168.215.0/24, Size: 24
   Base: 192.168.216.0/24, Size: 24
   Base: 192.168.223.0/24, Size: 24
   Base: 192.168.227.0/24, Size: 24
   Base: 192.168.228.0/24, Size: 24
   Base: 192.168.229.0/24, Size: 24
   Base: 192.168.237.0/24, Size: 24
   Base: 192.168.239.0/24, Size: 24
   Base: 192.168.242.0/24, Size: 24
   Base: 192.168.247.0/24, Size: 24
   Base: fd07:b51a:cc66:d000::/56, Size: 64

WARNING: DOCKER_INSECURE_NO_IPTABLES_RAW is set
//OrbStack 환경에서 iptables 관련 warning이 표시되었으나 기본 컨테이너 실행 및 네트워크 동작에는 영향이 없음을 확인하였다.
```

- 리눅스 보안 때문에 방화벽 iptables가 비활성화되어 있어서 나는 경고
- 실제 과제 수행에 있어서 관련없음
- 이미지 : 다운로드/목록 확인(예: docker images)

```jsx
jeay5290857@c4r2s5 ~ % docker images
REPOSITORY               TAG       IMAGE ID       CREATED       SIZE
hello-world              latest    e2ac70e7319a   7 days ago    10.1kB
docker/getting-started   latest    3e4394f6b72f   3 years ago   47MB
```

- 컨테이너 : 실행/중지/목록 확인 (예: docker ps, docker ps -a)
    - docker ps : 현재 살아있는 서비스 확인
    - docker ps -a : 이전 흔적까지 확인

```jsx
jeay5290857@c4r2s5 ~ % docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

jeay5290857@c4r2s5 ~ % docker ps -a
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                      PORTS     NAMES
1d9efdde49f2   hello-world              "/hello"                 2 minutes ago    Exited (0) 2 minutes ago              friendly_lumiere
54e3624de176   docker/getting-started   "/docker-entrypoint.…"   5 minutes ago    Exited (0) 2 minutes ago              peaceful_antonelli
4ea44af9bf06   hello-world              "/hello"                 6 minutes ago    Exited (0) 6 minutes ago              amazing_golick
4899a5b46304   hello-world              "/hello"                 6 minutes ago    Exited (0) 6 minutes ago              nostalgic_satoshi
91ff76871c11   docker/getting-started   "/docker-entrypoint.…"   17 minutes ago   Exited (0) 10 minutes ago             charming_mahavira
```

- 운영 : 로그 확인 ( 예: docker logs), 리소스 확인(예 : docker stats)
    - docker logs [컨테이너ID] : 컨테이너 내부 프로그램, 컨테이너 내부 실행 결과
    - docker stats : 실행 중인 컨테이너의 CPU, 메모리, 네트워크 사용량을 실시간으로 보여주는 명령

```jsx
//docker logs []
jeay5290857@c4r2s5 ~ % docker logs 1d9efdde49f2

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

//docker stats
jeay5290857@c4r2s5 ~ % docker stats

CONTAINER ID   NAME                CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O     PIDS 
91ff76871c11   charming_mahavira   0.00%     6.156MiB / 15.67GiB   0.04%     1.13kB / 126B   1.86MB / 0B   7 
 

```

### 3-4. hello-world 실행

- hello-world
    - docker run hello-world 명령으로 Docker 기본 컨테이너 실행을 확인하였다.
    - 로컬에 이미지가 없을 경우 Docker Hub에서 자동 다운로드가 수행되며, 실행 후 Hello 메시지를 출력하고 컨테이너는 종료된다.

```jsx
jeay5290857@c4r2s5 ~ % docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

- `ubuntu` 컨테이너를 실행하고 내부 진입 후 간단 명령(예: `ls`, `echo`) 수행 결과를 기록한다.
    - docker run
    - -it : 대화형 터미널 연결
    - ubuntu : 우분투 이미지 사용
    - bash :  bash셸 실행

```jsx
//ubuntu 컨테이너 실행 및 내부 진입
jeay5290857@c4r2s5 ~ % docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
817807f3c64e: Pull complete 
Digest: sha256:186072bba1b2f436cbb91ef2567abca677337cfc786c86e107d25b7072feef0c
Status: Downloaded newer image for ubuntu:latest
root@2758111624ba:/# 

//간단 명령 실행
root@2758111624ba:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr

root@2758111624ba:/# echo hello
hello

root@2758111624ba:/# pwd
/
```

- 컨테이너 종료/유지(attach/exec 등)의 차이를 스스로 관찰하고 간단히 정리한다.
    - 종료
        - docker stop [컨테이너 이름] : 정상 종료
            
            ```jsx
            jeay5290857@c4r2s5 ~ % docker stop myubuntu1
            myubuntu1
            ```
            
        - docker kill [컨테이너이름] : 즉시 종료
            - attach중이었다면 메인 프로세스 종료 → 컨테이너 종료
            - exec중이었다면 bash만 종료 → 컨테이너는 유지될 수 도 있음
            
            ```jsx
            jeay5290857@c4r2s5 ~ % docker kill myubuntu2
            myubuntu2
            ```
            
        - docker rm [컨테이너 이름] : 종료 후 삭제
    - 유지
        - attach : 원래 실행 중인 프로세스에 그대로 붙음, 새로운 셸x
            - 위험, 잘못 종료 시 컨테이너 종료 가능
        - exit : exec : 컨테이너 안에서 새로운 bash셸 실행
            - 안전, 사용 다

```jsx
jeay5290857@c4r2s5 ~ % docker run -it --name myubuntu1 ubuntu bash
root@c8b8367ac205:/# echo hello
hello
root@c8b8367ac205:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
```

```jsx
jeay5290857@c4r2s5 ~ % docker attach myubuntu1
root@c8b8367ac205:/# echo hello
hello
root@c8b8367ac205:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
```

```jsx
jeay5290857@c4r2s5 ~ % docker run -it --name myubuntu ubuntu bash
root@bc0464938172:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
```

```jsx
jeay5290857@c4r2s5 ~ % docker exec -it myubuntu bash
root@bc0464938172:/# echo hello
hello
root@bc0464938172:/# exit
exit
jeay5290857@c4r2s5 ~ % docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS         PORTS     NAMES
bc0464938172   ubuntu    "bash"    2 minutes ago   Up 2 minutes             myubuntu
```

### 3-5. Dockerfile 빌드/실행

- Docker
    - 컨테이너를 만들고 실행하는 플랫폼
- Dockerfile
    - 이미지를 만드는 설계 파일
- Docker Image
    - 컨테이너를 만들기 위한 설계도
    - 즉, 실행용 템플릿
- Docker Container
    - 이미지를 실제 실행한 인스턴스
- 어떤 “기존 베이스(이미지/예시 Dockerfile)”를 선택했는지
    - (A) 웹 서버 베이스 이미지 활용(예: NGINX/Apache 등) + 정적 콘텐츠/설정만 교체
    
    ```jsx
    docker-workstation/
    ├── Dockerfile
    ├── [README.md](http://readme.md/)
    ├── src/
    │   └── index.html
    └── screenshots/ 
    ```
    
    - 파일을 기능별로 분리해서 재현성과 가독성을 높임
        - /app : 백엔드 파일
        - /src : 프론트 파일
- 내가 적용한 커스텀 포인트 각각의 목적(간단 요약)
    - index.html
        - 기본 nginx 페이지 대신 app/index.html 파일을 복사하여 사용자 정의 웹 페이지가 출력되도록 하였다.
    - Dockerfile
        - 로컬 정적 파일을 nginx 기본 웹 경로에 복사하여 기본 페이지를 대체하였다.
- 빌드/실행 명령 + 핵심 결과(출력/스크린샷)
    - 커스텀 이미지 빌드 성공
        - docker build -t my-web:1.0 .
            - docker build : 이미지 생성
            - -t [이름 : 버전] : 이미지 이름 및 태그
            - . : 현재 디렉토리 기준으로 Dockerfile 읽기
            
            ```jsx
            jeay5290857@c4r2s5 docker-workstation % docker build -t my-web:1.0 .
            [+] Building 7.7s (7/7) FINISHED                                            docker:orbstack
             => [internal] load build definition from Dockerfile                                   0.2s
             => => transferring dockerfile: 191B                                                   0.0s
             => [internal] load metadata for docker.io/library/nginx:alpine                        2.7s
             => [internal] load .dockerignore                                                      0.1s
             => => transferring context: 2B                                                        0.0s
             => [internal] load build context                                                      0.2s
             => => transferring context: 225B                                                      0.0s
             => [1/2] FROM docker.io/library/nginx:alpine@sha256:e7257f1ef28ba17cf7c248cb8ccf6f0c  3.8s
             => => resolve docker.io/library/nginx:alpine@sha256:e7257f1ef28ba17cf7c248cb8ccf6f0c  0.2s
             => => sha256:e7257f1ef28ba17cf7c248cb8ccf6f0c6e0228ab9c315c152f9c2 10.33kB / 10.33kB  0.0s
             => => sha256:7e89aa6cabfc80f566b1b77b981f4bb98413bd2d513ca9a30f63fe5 2.50kB / 2.50kB  0.0s
             => => sha256:d5030d429039a823bef4164df2fad7a0defb8d00c98c1136aec06 12.32kB / 12.32kB  0.0s
             => => sha256:8892f80f46a05d59a4cde3bcbb1dd26ed2441d4214870a4a7b318ea 1.87MB / 1.87MB  0.5s
             => => sha256:589002ba0eaed121a1dbf42f6648f29e5be55d5c8a6ee0f8eaa0285 3.86MB / 3.86MB  0.9s
             => => sha256:91d1c9c22f2c631288354fadb2decc448ce151d7a197c167b206588e09d 626B / 626B  0.7s
             => => sha256:cf1159c696ee2a72b85634360dbada071db61bceaad253db7fda65c45a5 953B / 953B  1.0s
             => => sha256:3f4ad4352d4f91018e2b4910b9db24c08e70192c3b75d0d6fff0120c838 402B / 402B  1.2s
             => => extracting sha256:589002ba0eaed121a1dbf42f6648f29e5be55d5c8a6ee0f8eaa0285cc21a  0.1s
             => => sha256:4d9d41f3822d171ccc5f2cdfd75ad846ac4c7ed1cd36fb998fe2c0c 1.40kB / 1.40kB  1.5s
             => => sha256:c2bd5ab177271dd59f19a46c214b1327f5c428cd075437ec0155ae7 1.21kB / 1.21kB  1.4s
             => => extracting sha256:8892f80f46a05d59a4cde3bcbb1dd26ed2441d4214870a4a7b318eaa476a  0.1s
             => => extracting sha256:91d1c9c22f2c631288354fadb2decc448ce151d7a197c167b206588e09dc  0.0s
             => => sha256:3370263bc02adcf5c4f51831d2bf1d54dbf9a6a80b0bf32c5c9b9 20.25MB / 20.25MB  2.1s
             => => extracting sha256:cf1159c696ee2a72b85634360dbada071db61bceaad253db7fda65c45a58  0.0s
             => => extracting sha256:3f4ad4352d4f91018e2b4910b9db24c08e70192c3b75d0d6fff0120c838a  0.0s
             => => extracting sha256:c2bd5ab177271dd59f19a46c214b1327f5c428cd075437ec0155ae71d0cd  0.0s
             => => extracting sha256:4d9d41f3822d171ccc5f2cdfd75ad846ac4c7ed1cd36fb998fe2c0ce4501  0.0s
             => => extracting sha256:3370263bc02adcf5c4f51831d2bf1d54dbf9a6a80b0bf32c5c9b9400630e  0.5s
             => [2/2] COPY app/ /usr/share/nginx/html/                                             0.3s
             => exporting to image                                                                 0.2s
             => => exporting layers                                                                0.1s
             => => writing image sha256:4f562d7e216fb0086dbeff7e2085dd7cb8894eee6448271b98471832d  0.0s
             => => naming to docker.io/library/my-web:1.0                                          0.0s
            
            ```
            
    - 컨테이너 실행 성공
        - docker run -d -p 8080:80 --name my-web my-web:1.0
            - docker run : 컨테이너 생성 + 실행
            - -d : 백그라운드 실행 (터미널 점유 안함)
            - -p 8080:80 : 맥의 8080포트를 컨테이너 80포트와 연결
            - —name my-web : 컨테이너 이름 지정
            - my-web:1.0 : 빌드한 이미지 이름
            
            ```jsx
            jeay5290857@c4r2s5 docker-workstation % docker run -d -p 8080:80 --name my-web my-web:1.0
            a0ca73d9d70ab207bf1b45eaa3ddad6c96f87d361a7afedd0f64be42ec6dc9e0
            
            jeay5290857@c4r2s5 docker-workstation % docker ps
            CONTAINER ID   IMAGE        COMMAND                  CREATED         STATUS         PORTS                                     NAMES
            a0ca73d9d70a   my-web:1.0   "/docker-entrypoint.…"   9 minutes ago   Up 9 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   my-web
            ```
            
    - dockerfile -빌드→ 이미지 -run→ 컨테이너

### 3-6. 포트 매핑 접속(2회)

- 컨테이너 내부 서비스는 기본적으로 외부(macOS)에서 직접 접근 불가
- http://localhost로는 컨테이너 내부 80번으로 자동 연결되지 않음
- -p 8080:80 포트 매핑을 통해 호스트(macOS) 8080에서 컨테이너 80으로 연결

![Screenshot 2026-03-31 at 3.27.30 PM.png](attachment:e5a87a32-6413-4930-9961-ed8b9842eff0:Screenshot_2026-03-31_at_3.27.30_PM.png)

![Screenshot 2026-03-31 at 3.57.44 PM.png](attachment:b8a63aef-67ee-488e-b5b8-515f6462f8e7:Screenshot_2026-03-31_at_3.57.44_PM.png)

- 8080:80
    - 브라우저에서 내 컴퓨터에서 접속하는 포트
    - 내 컴퓨터에서 컨테이너 내부 웹서버(nginx)가 사용하는 포트
- 호스트IP와 컨테이너 IP를 분리
    - 보안 : 필요한 포트만 노출
    - 충돌 방지 : 여러 컨테이너가 같은 포트를 사용 가능 방지
    - 명시성 : 어떤 포트를 외부에 공개할지 명확
- 여러 컨테이너를 연속으로 돌리다니 보니 이미 사용중인 포트라는 경고
    - docker ps로 확인 후 사용하지 않는 컨테이너는 삭제하고 다시 실행

### 3-7. 바인드 마운트 반영

- 호스트 디렉토리를 컨테이너 내부 경로와 연결하여 파일 수정 사항이 즉시 반영되도록 하는 방식
    - build할 필요X
    
    ```jsx
    jeay5290857@c4r2s5 docker-workstation % docker run -d -p 8080:80 --name my-web-bind -v $(pwd)/app:/usr/share/nginx/html my-web:1.0
    fd407b4526143e16191d534262eb4815db322b4bc876a002b4a1714f5d9f4b6b
    ```
    

### 3-8. 볼륨 영속성

- 도커 볼륨
    - 저장 공간
    - 컨테이너 밖에서 도커가 관리
    - 컨테이너 삭제 후에도 데이터는 유지됨
- Docker 볼륨을 생성하고 컨테이너에 연결한다.
    
    ```jsx
    //볼륨 생성
    jeay5290857@c4r2s5 docker-workstation % docker volume create mydata
    mydata
    
    //볼륨 연결
    jeay5290857@c4r2s5 docker-workstation % docker run -d -p 8080:80 --name my-web-volume -v mydata:/data my-web:1.0
    847d4d64341e7289a544820ad2cf9695f7abcc8cd5d2eaac67de30ceafaa8463
    
    jeay5290857@c4r2s5 docker-workstation % docker volume ls
    DRIVER    VOLUME NAME
    local     mydata
    ```
    
- 컨테이너 삭제 전/후로 데이터를 확인하여 데이터가 유지됨을 증명한다.
    
    ```jsx
    //데이터 생성
    jeay5290857@c4r2s5 docker-workstation % docker exec -it my-web-volume sh -c "echo hello-volume > /data/hello.txt && cat /data/hello.txt"
    hello-volume
    
    //컨테이너 삭제
    jeay5290857@c4r2s5 docker-workstation % docker stop my-web-volume
    my-web-volume
    jeay5290857@c4r2s5 docker-workstation % docker rm my-web-volume
    my-web-volume
    jeay5290857@c4r2s5 docker-workstation % docker ps
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
    
    //새로운 컨테이너 실행
    jeay5290857@c4r2s5 docker-workstation % docker run -d -p 8080:80 --name my-web-volume -v mydata:/data my-web:1.0
    b7396e483a1fc3bccd32d1f4d0a48fa301bb7662bf06bd614a6ff1e4978a3515
    
    //데이터 유지 확인
    jeay5290857@c4r2s5 docker-workstation % docker exec -it my-web-volume sh -c "ls /data && cat /data/hello.txt" 
    50x.html    hello.txt   index.html
    hello-volume
    ```
    

### 3-9. Git 설정 + VSCode GitHub 연동

- git
    - 분산 버전 관리 시스템
    - 소스 코드의 변경 사항을 추적하고 관리
    - 변경 내용을 효과적으로 병합하고 관리
- github
    - 소스 코드를 공유하는 플랫폼
    - 이슈 트래킹, pull request 등
- Git 사용자 정보/ 기본 브랜치 설정

```jsx
jeay5290857@c4r2s5 docker-workstation % git config --global user.name "jeayoungKim529"
jeay5290857@c4r2s5 docker-workstation % git config --global user.email "jeay529@gmail.com"
jeay5290857@c4r2s5 docker-workstation % git config --global init.defaultBranch main
```

```jsx
jeay5290857@c4r2s5 docker-workstation % git config --list
user.name=jeayoungKim529
user.email=jeay529@gmail.com
init.defaultbranch=main
//
remote.origin.url=https://github.com/jeayoungKim529/Codyssey.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
```

- GitHub 로그인 및 저장소 연동

```jsx
jeay5290857@c4r2s5 docker-workstation % git remote -v
origin	https://github.com/jeayoungKim529/Codyssey.git (fetch)
origin	https://github.com/jeayoungKim529/Codyssey.git (push)
```