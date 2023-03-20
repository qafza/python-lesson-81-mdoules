
v = 42
idiom = 'Roma locuta causa finita est'

class Matrix:
    def __init__(self, n, m):
        self.rows = []
        for i in range(n):
            self.rows.append([0 for i in range(m)])

    def get(self, row, col):
        return self.rows[row][col]

    def set(self, row, col, value):
        self.rows[row][col] = value

    def __str__(self):
        s = ""
        for row in self.rows:
            s += str(row)
            s += '\n';
        return s

def sequence(n):
    return [i for i in range(n+1)]


if __name__ == '__main__':
    print('I am a magic module')
