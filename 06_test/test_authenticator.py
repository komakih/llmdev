from authenticator import Authenticator
import pytest

# ユーザーが正しく登録されているか
def test_add_user():
    add_user = Authenticator()

    add_user.register("apple", "orange")

    assert "apple" in add_user.users
    assert add_user.users["apple"] == "orange"

# 重複ユーザー登録の確認
def test_duplicate_user():
    duplicate_user = Authenticator()
    
    duplicate_user.register("apple", "orange")
    
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        duplicate_user.register("apple", "orange")

# ログイン確認
def test_login_user():
    login_user = Authenticator()

    login_user.register("apple", "orange")

    assert login_user.login("apple", "orange")

# 間違ったパスワードでのログイン確認
def test_misspassword_user():
    misspassword_user = Authenticator()

    misspassword_user.register("apple", "orange")

    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        misspassword_user.login("apple", "bananas")