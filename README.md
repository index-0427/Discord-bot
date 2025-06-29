# Discord AI Chat Bot

このプロジェクトは、OpenAIのGPTモデルを利用したDiscordチャットボットです。特定のAIペルソナに基づいてユーザーと会話をします。

## 機能

*   **AIチャット:** OpenAIのGPTモデルを利用して、ユーザーのメッセージに応答します。
*   **会話履歴の保持:** チャンネルごとに会話履歴を保持し、文脈を理解した応答が可能です。
*   **会話履歴のクリア:** `$clear` コマンドで現在のチャンネルの会話履歴をリセットできます。
*   **シンプルな応答:** `$hello` コマンドで簡単な挨拶をします。

## セットアップ

### 前提条件

*   Python 3.8+
*   Git

### 1. リポジトリのクローン

```bash
git clone https://github.com/your-username/Discord-bot.git # あなたのリポジトリURLに置き換えてください
cd Discord-bot
```

### 2. 仮想環境の作成とアクティベート

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定

プロジェクトのルートディレクトリに `.env` ファイルを作成し、以下の情報を記述してください。

```
DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE
```

*   `YOUR_DISCORD_BOT_TOKEN_HERE`: Discord開発者ポータルで取得したボットのトークン。
*   `YOUR_OPENAI_API_KEY_HERE`: OpenAIのAPIキー。

## 実行方法

仮想環境がアクティベートされていることを確認し、以下のコマンドでボットを起動します。

```bash
python3 main.py
```

## ボットコマンド

*   `$hello`: ボットが「Hello!」と応答します。
*   `$clear`: 現在のチャンネルの会話履歴をリセットします。

## 設定

*   **AIペルソナ:** `config/ai_persona.txt` ファイルを編集することで、ボットの性格や口調を設定できます。
*   **OpenAIモデル:** `main.py` 内で利用するOpenAIモデルを設定しています。現在の設定は `GEMINI.md` を参照してください。

## ライセンス

このプロジェクトは [LICENSE](LICENSE) ファイルに記載されているライセンスの下で公開されています。
