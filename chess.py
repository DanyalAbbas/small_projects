import pygame

# --- Configuration ---
WIDTH, HEIGHT = 512, 512
DIMENSION = 8 
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
COLORS = [pygame.Color("white"), pygame.Color("gray")]

class GameState:
    def __init__(self):
        # 8x8 board, 'w' = white, 'b' = black, 'R' = Rook, etc.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.move_log = []

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.white_to_move = not self.white_to_move

class Move:
    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Python Chess")
    clock = pygame.time.Clock()
    gs = GameState()
    
    selected_sq = () # (row, col)
    player_clicks = [] # [(6, 4), (4, 4)]
    
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                
                if selected_sq == (row, col): # Undo click
                    selected_sq = ()
                    player_clicks = []
                else:
                    selected_sq = (row, col)
                    player_clicks.append(selected_sq)
                
                if len(player_clicks) == 2: # Move piece
                    move = Move(player_clicks[0], player_clicks[1], gs.board)
                    gs.make_move(move)
                    selected_sq = ()
                    player_clicks = []

        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        pygame.display.flip()

def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)

def draw_board(screen):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = COLORS[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                # Fallback: Draw text if images aren't loaded
                font = pygame.font.SysFont("Arial", 24, bold=True)
                text_surface = font.render(piece, True, pygame.Color("black" if piece[0] == 'b' else "blue"))
                screen.blit(text_surface, pygame.Rect(c*SQ_SIZE + 10, r*SQ_SIZE + 10, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()