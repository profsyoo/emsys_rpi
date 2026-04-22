# Git & GitHub 실습 (Raspberry Pi 5)

본 자료는 **임베디드시스템** 교과목에서  
Git과 GitHub의 기본 사용법을 익히기 위한 실습용 안내서입니다.

Raspberry Pi 5에서 GitHub 리포지터리를  
**clone / pull / push** 하는 과정을 실습합니다.

---

## 1. 실습 목표

- Git 기본 명령어 이해
- GitHub 리포지터리 사용법 습득
- Raspberry Pi 기반 개발 환경에서 협업 흐름 경험

---

## 2. 사전 준비

### 2.1 환경
- Raspberry Pi 5
- Raspberry Pi OS
- 인터넷 연결

### 2.2 GitHub 계정
- 개인 GitHub 계정 필요
- https://github.com

### 2.3 Git 설치 확인

```bash
git --version
```

설치되어 있지 않다면:

```bash
sudo apt update
sudo apt install -y git
```

---

## 3. Git 사용자 정보 설정 (최초 1회)

```bash
git config --global user.name "본인 이름"
git config --global user.email "본인 GitHub 이메일"
```

확인:

```bash
git config --global --list
```

---

## 4. 리포지터리 Clone

```bash
cd ~
mkdir emsys
cd emsys
git clone https://github.com/profsyoo/emsys_rpi.git
cd emsys_rpi
```

---

## 5. 실습 디렉터리 이동

```bash
cd 99_intro2git
```

---

## 6. 최신 상태로 Pull

```bash
git pull
```

> ⚠️ 작업 시작 전 항상 `git pull`

---

## 7. 파일 생성 실습

```bash
nano myinfo.txt
```

내용 입력 예시:

```
이름: 홍길동
학번: 20251234
Raspberry Pi 5 Git 실습
```

저장: Ctrl + O → Enter  
종료: Ctrl + X

---

## 8. 상태 확인

```bash
git status
```

---

## 9. Commit

```bash
git add myinfo.txt
git commit -m "Add myinfo.txt for git practice"
```

---

## 10. Push 개념 설명

- 원본 리포지터리는 교수자 소유
- 학생은 직접 push 불가
- Fork 후 push 수행

---

## 11. Fork 후 Push 실습

### 11.1 Fork
- GitHub에서 `profsyoo/emsys_rpi` 접속
- **Fork** 버튼 클릭

### 11.2 remote 변경

```bash
git remote -v
git remote set-url origin https://github.com/본인ID/emsys_rpi.git
git remote -v
```

### 11.3 Push

```bash
git push origin main
```

---

## 12. 정리

- `clone` : 리포지터리 복사
- `pull`  : 최신 내용 가져오기
- `push`  : 변경 사항 업로드
- Git 기반 협업 개발 흐름 이해

---

임베디드시스템 수업  
Raspberry Pi 5 Git 실습
