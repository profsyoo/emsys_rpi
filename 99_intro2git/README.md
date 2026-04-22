# Git & GitHub 실습 (Raspberry Pi 5)

본 자료는 **임베디드시스템** 교과목에서  
Raspberry Pi 5 환경에서 Git과 GitHub의 기본 사용법을 익히기 위한 실습 안내서입니다.

본 실습을 통해 학생들은 **clone / pull / commit / push**의 차이와 흐름을 이해합니다.

---

## 1. 실습 목표

- Git 기본 개념 이해 (commit, push 차이)
- GitHub 리포지터리 사용법 습득
- Raspberry Pi 기반 협업 개발 흐름 경험

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

> ⚠️ 실습 시작 전 항상 `git pull` 수행

---

## 7. 파일 생성 실습

```bash
nano myinfo.txt
```

내용 예시:

```
이름: 홍길동
학번: 20251234
Raspberry Pi 5 Git 실습
```

저장: Ctrl + O → Enter  
종료: Ctrl + X

---

## 8. 현재 상태 확인

```bash
git status
```

---

## 9. Commit이란?

### ✅ Commit 한 줄 설명
> **commit은 “현재 작업 상태를 Git에 저장하는 것”이다.**

### ✅ Commit의 특징
- 내 Raspberry Pi(로컬 컴퓨터)에 저장됨
- GitHub에는 아직 올라가지 않음
- 작업 기록(히스토리)을 남김

### ✅ Commit 수행

```bash
git add myinfo.txt
git commit -m "Add myinfo.txt for git practice"
```

---

## 10. Commit과 Push의 차이 (중요)

| 구분 | 의미 |
|---|---|
| commit | 내 컴퓨터에 변경 사항 저장 |
| push | commit한 내용을 GitHub에 업로드 |

👉 **commit만 하면 GitHub에는 반영되지 않는다**

---

## 11. git push origin main의 의미

```bash
git push origin main
```

이 명령어는 다음 의미를 가집니다.

- `git push` : 업로드하라
- `origin` : 원격 저장소(GitHub)
- `main` : 기본 브랜치

### ✅ 한 문장으로 설명하면

> **“내 컴퓨터에 commit한 내용을  
> GitHub(origin)의 main 브랜치로 업로드하라”**

---

## 12. Push 실습을 위한 Fork

### 12.1 Fork 이유
- 본 리포지터리는 교수자 소유
- 학생은 직접 push 불가
- Fork 후 본인 리포지터리에 push 수행

### 12.2 Fork 방법
1. GitHub에서 `profsyoo/emsys_rpi` 접속
2. **Fork** 버튼 클릭

---

## 13. 원격 저장소 변경

```bash
git remote -v
git remote set-url origin https://github.com/본인ID/emsys_rpi.git
git remote -v
```

---

## 14. Push

```bash
git push origin main
```

> 최초 push 시 GitHub ID 및 토큰 입력 필요

---

## 15. 전체 흐름 정리

```
clone → pull → 수정 → add → commit → push
```

- commit : 저장
- push : 업로드

---

임베디드시스템 수업  
Raspberry Pi 5 Git 실습
