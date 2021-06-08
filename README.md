# streamlit_custom_notifiers
A component which sticks on top, and shows a message, includes spinner.

The components uses the theme colors, it's still in development.

Tested on:

`Python 3.8`

`streamlit 0.82.0`

----

- You need the styles.css for the icon, and you need to inject it like in the `app.py`.
- Usage:
    wrap your function with this, and after the function ends, the message will dissapear.

    ```
    with cc.stNotification(text=str, spinner=bool):
        """your code""
    ```
        - text: the text that will be desplayed.
        - spinner: boolean, if True will show the spinner icon.

![Анимация](https://user-images.githubusercontent.com/44586585/121157052-e718cb00-c851-11eb-9b09-8a8c3b0ca270.gif)

