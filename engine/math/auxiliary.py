# ═══════════════════════════════════════════════════════════════
# FUNÇÕES MATEMÁTICAS AUXILIARES
# ═══════════════════════════════════════════════════════════════
# Funções matemáticas auxiliares para operações gráficas.
#
# Inclui:
# - Interpolação linear de cores (usado em gradientes)
# ═══════════════════════════════════════════════════════════════

def interpolar_cor(cor1, cor2, t):
    """
    Interpolação linear entre duas cores RGB.
    
    Usado em: gradientes (scanline fill), efeitos visuais.
    Relacionado ao Requisito (c) - Scanline Fill com gradiente
    
    Fórmula: cor = cor1 + t * (cor2 - cor1) para cada canal RGB
    
    Args:
        cor1: tupla (R, G, B) inicial
        cor2: tupla (R, G, B) final
        t: fator de interpolação (0.0 = cor1, 1.0 = cor2)
    
    Returns:
        tupla (R, G, B) interpolada
    
    Exemplo:
        interpolar_cor((0, 0, 0), (255, 255, 255), 0.5)  # → (127, 127, 127)
    """
    r1, g1, b1 = cor1
    r2, g2, b2 = cor2
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return (r, g, b)