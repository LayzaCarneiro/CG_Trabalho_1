# ═══════════════════════════════════════════════════════
# TRANSFORMAÇÕES GEOMÉTRICAS 2D
# ═══════════════════════════════════════════════════════
# Implementação das três principais transformações geométricas
# (Requisito d - Transformações Geométricas)
#
# Transformações implementadas:
# - Translação: move objetos no espaço
# - Escala: redimensiona objetos
# - Rotação: gira objetos em torno de um pivô
#
# Utiliza matrizes homogêneas 3x3 para compor transformações.
# ═══════════════════════════════════════════════════════

import math

# ─── Matrizes de Transformação 2D (Homogêneas 3x3) ───
def identidade():
    """Matriz identidade 3x3 (nenhuma transformação)."""
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

def translacao(tx, ty):
    """
    Cria matriz de translação.
    
    REQUISITO: (d) Transformações Geométricas - Translação
    
    Move objetos tx unidades em X e ty unidades em Y.
    Usado no jogo para: movimento da jangada, câmera, animações.
    """
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ]

def escala(sx, sy):
    """
    Cria matriz de escala.
    
    REQUISITO: (d) Transformações Geométricas - Escala
    
    Redimensiona objetos sx vezes em X e sy vezes em Y.
    Usado no jogo para: zoom, efeitos de HUD, ajuste de tamanhos.
    """
    return [
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ]

def rotacao(theta):
    """
    Cria matriz de rotação.
    
    REQUISITO: (d) Transformações Geométricas - Rotação
    
    Rotaciona objetos theta radianos no sentido anti-horário.
    Usado no jogo para: rotação da jangada ao colidir, animações.
    
    Args:
        theta: ângulo em radianos
    """
    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [ c, -s, 0],
        [ s,  c, 0],
        [ 0,  0, 1]
    ]

# ─── Operações com Matrizes ───
def multiplica_matrizes(a, b):
    """Multiplica duas matrizes 3x3 para compor transformações."""
    r = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                r[i][j] += a[i][k] * b[k][j]
    return r

def cria_transformacao():
    """Inicializa uma transformação identidade."""
    return identidade()

def aplica_transformacao(m, pontos):
    """
    Aplica matriz de transformação a uma lista de pontos.
    
    Args:
        m: matriz 3x3 de transformação
        pontos: lista de tuplas (x, y)
    
    Returns:
        lista de pontos transformados
    """
    novos = []
    for x, y in pontos:
        v = [x, y, 1]
        x_novo = m[0][0]*v[0] + m[0][1]*v[1] + m[0][2]
        y_novo = m[1][0]*v[0] + m[1][1]*v[1] + m[1][2]
        novos.append((round(x_novo), round(y_novo)))
    return novos


# ─── Rotação em Torno de um Pivô ───
def rotacionar_pontos_em_torno_de(pontos, cx, cy, theta):
    """
    Rotaciona pontos em torno de um pivô (cx, cy).
    
    REQUISITO: (d) Transformações Geométricas - Rotação composta
    
    Algoritmo:
    1. Translada para origem (pivô em 0,0)
    2. Aplica rotação
    3. Translada de volta
    
    Usado no jogo para: rotação 360° da jangada ao colidir.
    
    Args:
        pontos: lista de tuplas (x, y)
        cx, cy: ponto pivô (centro de rotação)
        theta: ângulo em radianos
    
    Returns:
        lista de pontos rotacionados
    """
    t_neg = translacao(-cx, -cy)
    r = rotacao(theta)
    t_pos = translacao(cx, cy)
    m = multiplica_matrizes(t_pos, multiplica_matrizes(r, t_neg))
    return aplica_transformacao(m, pontos)

# =====================================================
# Polígono em coordenadas absolutas
# =====================================================
poligono_original = [
    (200, 150),
    (300, 170),
    (320, 240),
    (250, 290),
    (190, 230)
]

# centro (pivô)
cx = sum(p[0] for p in poligono_original) / len(poligono_original)
cy = sum(p[1] for p in poligono_original) / len(poligono_original)

angulo = 0
tempo = 0