# 게임월드 표현
world = [[] for _ in range(10000)]


# 게임 월드에 객체 담기
def add_obj(o, depth=0):
    world[depth].append(o)  # 지정된 깊이의 레이어에 객체 추가


# 게임 월드 객체들을 모두 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_obj(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('존재하지 않는 객체 삭제 요청')
