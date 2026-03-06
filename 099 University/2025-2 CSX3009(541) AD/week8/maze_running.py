# Puran Paodensakul
# 6611140
# 541


from collections import deque


class State:
    def __init__(self, y, x, step):
        self.y = y
        self.x = x
        self.step = step


def valid(y, x, maze, M, N):
    return 0 <= y < M and 0 <= x < N and maze[y][x] == 0


def shortest_path(maze, start, end):
    M = len(maze)
    N = len(maze[0])

    visited = [[False] * N for _ in range(M)]
    queue = deque()

    sy, sx = start
    ey, ex = end

    queue.append(State(sy, sx, 0))
    visited[sy][sx] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current = queue.popleft()

        if (current.y, current.x) == (ey, ex):
            return current.step

        for dy, dx in directions:
            ny, nx = current.y + dy, current.x + dx
            if valid(ny, nx, maze, M, N) and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append(State(ny, nx, current.step + 1))

    return -1


if __name__ == "__main__":
    M, N = map(int, input().split())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    maze = [list(map(int, input().split())) for _ in range(M)]

    print(shortest_path(maze, (sr, sc), (er, ec)))
