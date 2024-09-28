import flet as ft

class JogoDaVelha:
    def __init__(self):
        self.reiniciar_jogo()
        self.vitorias_x = 0
        self.vitorias_o = 0

    def reiniciar_jogo(self):
        self.tabuleiro = [" " for _ in range(9)]
        self.jogador_atual = "X"
        self.jogo_terminado = False

    def fazer_jogada(self, indice):
        if not self.jogo_terminado and self.tabuleiro[indice] == " ":
            self.tabuleiro[indice] = self.jogador_atual
            self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
            return True
        return False

    def verificar_vitoria(self):
        linhas_vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontais
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # verticais
            [0, 4, 8], [2, 4, 6]  # diagonais
        ]
        for linha in linhas_vitoria:
            if self.tabuleiro[linha[0]] == self.tabuleiro[linha[1]] == self.tabuleiro[linha[2]] != " ":
                return self.tabuleiro[linha[0]]
        if " " not in self.tabuleiro:
            return "Empate"
        return None

def main(page: ft.Page):
    page.title = "Jogo da Velha"
    jogo = JogoDaVelha()

    def atualizar_tabuleiro():
        for i, botao in enumerate(botoes):
            botao.text = jogo.tabuleiro[i]
            botao.disabled = jogo.tabuleiro[i] != " " or jogo.jogo_terminado
        status.value = f"Vez do jogador: {jogo.jogador_atual}"
        placar.value = f"Placar - X: {jogo.vitorias_x} | O: {jogo.vitorias_o}"
        page.update()

    def on_click(e):
        indice = int(e.control.data)
        if jogo.fazer_jogada(indice):
            atualizar_tabuleiro()
            resultado = jogo.verificar_vitoria()
            if resultado:
                jogo.jogo_terminado = True
                if resultado == "Empate":
                    status.value = "Jogo empatado!"
                else:
                    status.value = f"Jogador {resultado} venceu!"
                    if resultado == "X":
                        jogo.vitorias_x += 1
                    else:
                        jogo.vitorias_o += 1
                atualizar_tabuleiro()

    def reiniciar_jogo(e):
        jogo.reiniciar_jogo()
        atualizar_tabuleiro()

    botoes = [
        ft.ElevatedButton(
            text=" ",
            on_click=on_click,
            data=str(i),
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
            width=100,
            height=100,
        )
        for i in range(9)
    ]

    status = ft.Text(f"Vez do jogador: {jogo.jogador_atual}")
    placar = ft.Text(f"Placar - X: {jogo.vitorias_x} | O: {jogo.vitorias_o}")
    botao_reiniciar = ft.ElevatedButton("Reiniciar Jogo", on_click=reiniciar_jogo)

    tabuleiro = ft.Row(
        [ft.Column([botoes[i], botoes[i+1], botoes[i+2]]) for i in range(0, 9, 3)],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(tabuleiro, status, placar, botao_reiniciar)

ft.app(target=main)
