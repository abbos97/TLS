# 🛡 TLS 기반 사용자 인증 및 안전한 통신 시뮬레이터

## 🔹 프로젝트 개요
이 프로젝트는 TLS 보안 연결을 통해 사용자 인증을 수행하고, AES 암호화로 안전하게 메시지를 전송하는 시스템입니다.

사용자가 로그인하면, 서버는 해당 사용자를 확인하고 암호화된 메시지를 복호화하여 출력합니다.

---

## 🔹 사용된 주요 기술

- **TLS (Transport Layer Security)**: 안전한 통신 채널 제공  
- **bcrypt**: 비밀번호 해싱 및 검증  
- **AES (CBC 모드)**: 메시지 암호화 및 복호화  
- **Python socket & ssl**: 클라이언트-서버 구조 구현  

---

## 🔹 add_user.py

- 새로운 사용자를 등록하는 스크립트입니다.
- 실행 시, 콘솔에서 사용자 이름과 비밀번호를 입력합니다.
- 비밀번호는 `bcrypt`로 해시되어 `users.json` 파일에 저장됩니다.

```bash
python add_user.py
```

---

## 🔹 hashing.py

- `bcrypt`를 이용해 비밀번호를 안전하게:
  - 해시 (hash)
  - 검증 (verify)
하는 함수들이 정의되어 있습니다.

---

## 🔹 encryption.py

- 메시지를 AES 방식으로:
  - 암호화 (`encrypt_message`)
  - 복호화 (`decrypt_message`)
하는 기능이 포함되어 있습니다.

---

## 🔹 server.py

- TLS 서버를 실행하는 메인 파일입니다.
- 사용자의 `username`, `password`, 그리고 암호화된 메시지를 받아 인증 후 복호화합니다.
- 복호화된 메시지는 서버 콘솔에 출력됩니다.

```bash
python server/server.py
```

---

## 🔹 client.py

- 사용자 클라이언트입니다.
- 실행하면 아래 정보를 입력합니다:
  1. 사용자 이름
  2. 비밀번호
  3. 전송할 메시지
- 등록된 사용자일 경우, 메시지가 암호화되어 서버에 전송되고,
- 서버는 메시지를 복호화해 콘솔에 출력합니다.

```bash
python client/client.py
```

---

## 🔹 시연 예시

```
Username: max
Password: 1234
Message: hello server
```

→ 서버 콘솔 출력:
```
[✓] Decrypted message from max: hello server
```