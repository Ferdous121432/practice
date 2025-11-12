from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class SearchScreen(Screen):
    def search_image(self):
        # Get the user query from the TextInput
        query = self.manager.current_screen.ids.user_query.text

        # Search Wikipedia for the query
        page = wikipedia.page(query)
        img_url = page.images[0]
        print(f"Image URL: {img_url}")

        # Download the image
        img_data = requests.get(img_url)
        with open('aa.jpg', 'wb') as handler:
            handler.write(img_data.content)

        # Update the Image widget to display the downloaded image

        self.manager.current_screen.ids.img.source = 'aa.jpg'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
