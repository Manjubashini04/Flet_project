import  flet as  ft

def main(page:ft.Page):
    page.title='To Do List'
    def set_task(e):
        page.add(
            ft.Checkbox(label=task.value)
        )
        task.value=''
        page.update()



    task=ft.TextField(hint_text='What\'s needs to be done?',width=600,border_radius=30,border_color='Blue')

    add_button = ft.ElevatedButton(text="Task",icon=ft.icons.ADD,height=50,on_click=set_task)
    page.add(
        ft.Row(
            controls=[task,add_button])
    )



    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER



ft.app(target=main)