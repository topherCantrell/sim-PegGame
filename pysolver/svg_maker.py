import pathlib

class SVGBoard:
    def __init__(self, board):
        self.board = board

    def set_peg(self, name, has_peg=True):
        if has_peg:
            self.board = SVGMaker.uncomment(self.board, f'peg {name}')
        else:
            self.board = SVGMaker.uncomment(self.board, f'empty {name}')

    def set_move(self, move):
        self.board = SVGMaker.uncomment(self.board, f'move {move}')

    def set_scale(self, scale):
        self.board = self.board.replace("scale(0.5)", f"scale({scale})")        

    def set_text(self, text):
        self.board = self.board.replace("%%TEXT%%", text)

    def set_position(self, x, y):
        self.board = self.board.replace("translate(0,0)", f"translate({x},{y})")


class SVGMaker:

    @staticmethod
    def uncomment(template, s):
        i = template.find(f"<!-- {s}")
        if i<0:
            raise ValueError(f"Cannot find {s} in template")
        i = i + len(f"<!-- {s}")
        j = template.find("-->", i)
        return template[:i] + ' -->'+template[i:j] + template[j+3:]

    def __init__(self):
        script_dir = pathlib.Path(__file__).parent.resolve()
        with open(f"{script_dir}/template.svg", "r") as f:
            self.template = f.read()

        i = self.template.find("<!-- COPY_BEGIN -->")
        j = self.template.find("<!-- COPY_END -->")
        self.template_board = self.template[i + len("<!-- COPY_BEGIN -->"):j].strip()
        self.template_write = self.template[:i + len("<!-- COPY_BEGIN -->")] + self.template[j:]
        
    def make_board(self):
        return SVGBoard(self.template_board)    

    def make_svg(self, fname, boards, scale):
        nscale = scale / 2  # template is at scale 0.5, so we need to divide by 2 to get the correct scale

        num_rows = 1
        num_cols = len(boards)
        if len(boards) > 7:
            num_rows = 2
            num_cols = 7        

        width = 650 * num_cols * nscale
        height = 650 * num_rows * nscale

        print(">>>>>>", num_rows, num_cols, width, height)

        self.template_write = self.template_write.replace(' width="325"', f' width="{width}"')
        self.template_write = self.template_write.replace(' height="325"', f' height="{height}"')

        x,y = 0,0
        for board in boards:
            board.set_position(x,y)
            board.set_scale(nscale)
            x += 650*nscale
            if x >= 650*7*nscale:
                x = 0
                y += 650*nscale

        w = self.template_write.replace("<!-- OTHERS -->", "\n".join(board.board for board in boards))
        with open(fname, "w") as f:
            f.write(w)

if __name__ == "__main__":
    maker = SVGMaker()

    b0 = maker.make_board()
    b0.set_peg("0",False)
    for i in range(3,10):
        b0.set_peg(f"{i:X}")
    b0.set_move("520")
    b0.set_text("Hey!")

    b1 = maker.make_board()    
    for i in range(5):
        b1.set_peg(f"{i:X}")
    b1.set_text("There")

    b2 = maker.make_board() 
    b3 = maker.make_board() 
    b4 = maker.make_board() 
    b5 = maker.make_board() 
    b6 = maker.make_board() 
    b7 = maker.make_board() 
    b8 = maker.make_board() 
    b9 = maker.make_board() 
    
    maker.make_svg('test.svg', [b0, b1, b2, b3, b4, b5, ], 0.5)