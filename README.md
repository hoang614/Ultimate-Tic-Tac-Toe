# Ultimate Tic-Tac-Toe
## Tổng quan
Ultimate Tic-Tac-Toe là một phiên bản mở rộng của trò chơi Tic-Tac-Toe truyền thống. Trò chơi được chơi trên một lưới lớn 3×3, trong đó mỗi ô của lưới lớn là một lưới nhỏ 3×3. Người chơi cần thắng các lưới nhỏ để chiếm lĩnh các ô trong lưới lớn, với mục tiêu cuối cùng là thắng lưới lớn.

Dự án này triển khai Ultimate Tic-Tac-Toe với giao diện đồ họa sử dụng Pygame, cho phép:

- Người chơi (O) đấu với AI (X).
- Tùy chọn ai đi trước (AI hoặc người chơi).
- Hiển thị trạng thái trò chơi (lưới lớn, lưới nhỏ, nước đi trước, block tiếp theo).
## Tính năng
- Giao diện đồ họa: Lưới lớn 3×3, mỗi block chứa lưới nhỏ 3×3.
- Chế độ chơi: Người chơi đấu với AI.
- Tùy chọn lượt đi: Chọn AI hoặc người chơi đi trước.
- Hiển thị trạng thái:
  + Block tiếp theo được tô màu xanh.
  + Ô vừa đi được tô màu cam.
  + X/O lớn xuất hiện khi một block được thắng.
- Tương tác: Người chơi click chuột để chọn nước đi.
## Yêu cầu
- Python: Phiên bản 3.x.
- Pygame: Thư viện đồ họa (pip install pygame).
- Hình ảnh:
  + images/small_x.png, images/small_o.png: Hình X và O nhỏ.
  + images/large_x.png, images/large_o.png: Hình X và O lớn.
- Tệp cần thiết:
  + state.py: Chứa class State, State_2 và UltimateTTT_Move.
  + Module AI (botAI.py).
## Cài đặt
### Cài đặt Python và Pygame:
```bash
pip install pygame
```
## Cấu trúc thư mục
```
Ultimate-Tic-Tac-Toe/
│
├── images/
│   ├── small_x.png
│   ├── small_o.png
│   ├── large_x.png
│   └── large_o.png
│
├── state.py
├── botAI.py  # Module AI
├── test_game.py                      # Code chính
└── README.md
```
## Cách sử dụng
### 1. Chạy trò chơi
Mở terminal, di chuyển đến thư mục dự án và chạy:
```bash
  python test_game.py
```
### 2. Tùy chọn ai đi trước
Mở test_game.py và chỉnh tham số first_player trong hàm play_human_vs_ai
- AI đi trước
```bash
play_human_vs_ai('botAI', 2, first_player=1)
```
- Người chơi đi trước
```bash
play_human_vs_ai('botAI', 2, first_player=-1)
```
