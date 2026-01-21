import random

def print_board(board):
    """
    Fungsi untuk menampilkan papan Tic Tac Toe.
    Papan ditampilkan dengan angka 1-9 untuk kotak kosong,
    dan X atau O untuk kotak yang sudah diisi.
    """
    print("\nPapan Tic Tac Toe:")
    for i in range(3):
        row = []
        for j in range(3):
            if board[i][j] == ' ':
                # Hitung angka berdasarkan posisi (1-9)
                num = i * 3 + j + 1
                row.append(str(num))
            else:
                row.append(board[i][j])
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    """
    Fungsi untuk memeriksa apakah ada pemenang.
    Mengembalikan 'X' jika manusia menang, 'O' jika komputer menang,
    'Draw' jika seri, atau None jika belum ada hasil.
    """
    # Periksa baris
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    # Periksa kolom
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Periksa diagonal
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    # Periksa seri (semua kotak terisi)
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Draw'
    
    return None

def human_move(board):
    """
    Fungsi untuk menangani langkah manusia.
    Meminta input angka 1-9, validasi bahwa kotak kosong,
    dan tempatkan 'X' di posisi tersebut.
    """
    while True:
        try:
            move = int(input("Masukkan angka 1-9 untuk posisi Anda (X): "))
            if move < 1 or move > 9:
                print("Input harus antara 1-9.")
                continue
            # Konversi angka ke indeks (0-based)
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] != ' ':
                print("Kotak sudah terisi. Pilih kotak kosong.")
                continue
            board[row][col] = 'X'
            break
        except ValueError:
            print("Input harus berupa angka.")

def computer_move(board):
    """
    Fungsi untuk langkah komputer (O).
    Komputer akan mencoba menang jika mungkin,
    atau blokir manusia jika manusia akan menang,
    atau pilih kotak kosong secara acak.
    """
    # Fungsi helper untuk menemukan langkah pemenang
    def find_winning_move(player):
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    if check_winner(board) == player:
                        board[i][j] = ' '  # Reset
                        return (i, j)
                    board[i][j] = ' '  # Reset
        return None
    
    # Coba menang
    move = find_winning_move('O')
    if move:
        board[move[0]][move[1]] = 'O'
        return
    
    # Blokir manusia
    move = find_winning_move('X')
    if move:
        board[move[0]][move[1]] = 'O'
        return
    
    # Pilih acak
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_spots:
        move = random.choice(empty_spots)
        board[move[0]][move[1]] = 'O'

def main():
    """
    Fungsi utama untuk menjalankan game Tic Tac Toe.
    Inisialisasi papan, loop game, dan tampilkan hasil.
    """
    # Inisialisasi papan kosong
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    print("Selamat datang di Tic Tac Toe!")
    print("Anda adalah X, komputer adalah O.")
    print("Masukkan angka 1-9 untuk memilih posisi.")
    
    while True:
        print_board(board)
        
        # Langkah manusia
        human_move(board)
        
        # Cek hasil setelah langkah manusia
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'X':
                print("Selamat! Anda menang!")
            elif winner == 'O':
                print("Maaf, Anda kalah!")
            else:
                print("Seri!")
            break
        
        # Langkah komputer
        print("Komputer berpikir...")
        computer_move(board)
        
        # Cek hasil setelah langkah komputer
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'X':
                print("Selamat! Anda menang!")
            elif winner == 'O':
                print("Maaf, Anda kalah!")
            else:
                print("Seri!")
            break

if __name__ == "__main__":
    main()
