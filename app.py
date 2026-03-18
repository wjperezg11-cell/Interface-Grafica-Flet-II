import flet as ft


def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.window_width = 500
    page.window_height = 650
    page.padding = 30
    page.bgcolor = ft.Colors.GREY_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text(
        "Formulário de Contato",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_900
    )

    subtitulo = ft.Text(
        "Preencha os dados abaixo e envie sua mensagem.",
        size=14,
        color=ft.Colors.GREY_700
    )

    campo_nome = ft.TextField(
        label="Nome",
        prefix_icon=ft.Icons.PERSON,
        border_radius=10,
        filled=True,
        width=400
    )

    campo_email = ft.TextField(
        label="Email",
        prefix_icon=ft.Icons.EMAIL,
        border_radius=10,
        filled=True,
        width=400
    )

    campo_mensagem = ft.TextField(
        label="Mensagem",
        prefix_icon=ft.Icons.MESSAGE,
        multiline=True,
        min_lines=4,
        max_lines=6,
        border_radius=10,
        filled=True,
        width=400
    )

    mensagem_confirmacao = ft.Text(
        "",
        size=16,
        color=ft.Colors.GREEN_700,
        weight=ft.FontWeight.BOLD
    )

    def enviar_formulario(e):
        nome = campo_nome.value.strip()
        email = campo_email.value.strip()
        mensagem = campo_mensagem.value.strip()

        if not nome:
            campo_nome.error_text = "Informe o nome."
        else:
            campo_nome.error_text = None

        if not email:
            campo_email.error_text = "Informe o email."
        else:
            campo_email.error_text = None

        if not mensagem:
            campo_mensagem.error_text = "Digite uma mensagem."
        else:
            campo_mensagem.error_text = None

        if nome and email and mensagem:
            print("Dados enviados:")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Mensagem: {mensagem}")

            mensagem_confirmacao.value = "Formulário enviado com sucesso."

            campo_nome.value = ""
            campo_email.value = ""
            campo_mensagem.value = ""

        page.update()

    botao_enviar = ft.ElevatedButton(
        text="Enviar",
        icon=ft.Icons.SEND,
        width=200,
        height=45,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
        on_click=enviar_formulario
    )

    formulario = ft.Card(
        elevation=4,
        content=ft.Container(
            width=430,
            padding=25,
            content=ft.Column(
                controls=[
                    titulo,
                    subtitulo,
                    campo_nome,
                    campo_email,
                    campo_mensagem,
                    botao_enviar,
                    mensagem_confirmacao
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )

    page.add(formulario)


ft.app(target=main)
