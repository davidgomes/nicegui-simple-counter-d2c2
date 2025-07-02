from nicegui import ui, app
from .models import Counter

def create():
    @ui.page('/')
    def page():
        # Initialize counter in user storage, so it persists across page reloads
        if 'counter' not in app.storage.user:
            app.storage.user['counter'] = Counter().model_dump()
        
        counter_data = Counter(**app.storage.user['counter'])
        
        # UI elements
        ui.markdown('# Counter App')
        
        counter_label = ui.label(f'Count: {counter_data.value}').classes('text-2xl font-bold text-center').mark('counter-display')
        
        with ui.row().classes('gap-4 justify-center'):
            decrement_btn = ui.button('-', color='red').classes('text-xl px-4 py-2').mark('decrement-btn')
            increment_btn = ui.button('+', color='green').classes('text-xl px-4 py-2').mark('increment-btn')
        
        reset_btn = ui.button('Reset', color='grey').classes('mt-4').mark('reset-btn')
        
        def update_display():
            counter_label.set_text(f'Count: {counter_data.value}')
            app.storage.user['counter'] = counter_data.model_dump()
        
        def increment():
            counter_data.value += 1
            update_display()
            ui.notify(f'Incremented to {counter_data.value}', type='positive')
        
        def decrement():
            counter_data.value -= 1
            update_display()
            ui.notify(f'Decremented to {counter_data.value}', type='info')
        
        def reset():
            counter_data.value = 0
            update_display()
            ui.notify('Counter reset to 0', type='warning')
        
        # Connect event handlers
        increment_btn.on_click(increment)
        decrement_btn.on_click(decrement)
        reset_btn.on_click(reset)