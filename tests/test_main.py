import app.main


class TestMain:
    def test_function(self):
        ret = app.main.test_func()
        assert ret
