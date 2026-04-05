🌐 [English](README.md) | **日本語** | [中文](README.zh-CN.md) | [한국어](README.ko.md)

> [!NOTE]
> この翻訳はAIの支援を受けて作成されました。不自然な表現や誤訳がありましたら、ぜひIssueやPull Requestでお知らせください。コミュニティからの修正を歓迎します。

# 🧠 Obsidian Mind

[![Claude Code](https://img.shields.io/badge/claude%20code-required-D97706)](https://docs.anthropic.com/en/docs/claude-code)
[![Obsidian](https://img.shields.io/badge/obsidian-1.12%2B-7C3AED)](https://obsidian.md)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> **Claude Codeにすべてを記憶させるObsidianボールト。** セッションを開始して、日々のことを話すだけ — ノート、リンク、インデックス、プロジェクトコンテキストはClaudeが自動で処理します。すべての会話が前回の続きとして積み重なっていきます。

---

## 🔴 課題

Claude Codeは強力ですが、忘れてしまいます。毎回のセッションがゼロからの出発 — あなたの目標、プロジェクト、パターン、実績に関するコンテキストがありません。同じことを何度も説明し直し、3回前の会話で下した決定が失われます。知識が蓄積されないのです。

## 🟢 解決策

Claudeに脳を与えましょう。

```
あなた: "セッション開始"
Claude: *North Starを読み、アクティブなプロジェクトを確認し、最近の記憶をスキャン*
Claude: "アクティブなプロジェクトが5つあります。patient-registryにはStimulus移行に関する
         保留中のADRがあります。lab-inventoryは12日間アクティビティがありません。
         sample-trackerのデプロイ手順書を更新する必要があります。"
```

---

## ⚡ 実際の動作

**朝のキックオフ:**

```bash
/standup
# → North Star、アクティブプロジェクト、未完了タスク、最近のgit変更を読み込み
# → "アクティブなプロジェクトが5つあります。patient-registryは昨日3つのコミットがありました。
#    lab-inventoryには2週間前の古い作業ノートがあります。"
```

**プロジェクト間のコンテキスト切り替え:**

```bash
/context-switch patient-registry
# → プロジェクトREADMEを読み込み（Rails 7.1、research-app01にデプロイ、PIはDr. Smith）
# → 直近3つの作業ノートと未解決の意思決定を読み込み
# → "CSVバルクインポートのタイムアウト修正の途中でした。フォームバリデーションを
#    Stimulusに切り替えるかどうかの保留中の意思決定があります。"
```

**GitHubイシューを作業ノートとしてキャプチャ:**

```bash
/issue-capture https://github.com/hospital/patient-registry/issues/47
# → gh CLIでイシューを取得
# → work/projects/patient-registry/notes/2026-04-05-bulk-import-timeout.md を作成
# → project、github_issue、descriptionのフロントマターを自動入力
```

**ミーティング後のブレインダンプ:**

```bash
/dump Met with Dr. Smith about the patient registry. She wants bulk import
to handle 50k rows by end of month. Also, IT security said we need to add
audit logging for all PHI access — that's a HIPAA requirement. Decision:
use Active Job for the import instead of inline processing.
```

```
→ work/projects/patient-registry/notes/2026-04-05-bulk-import-requirements.md を作成
→ Decision Record を作成: 「バルクインポートにActive Jobを使用」
→ reference/compliance/hipaa-audit-logging.md をPHIアクセス要件で更新
→ org/people/Dr Smith.md をミーティングの内容で更新
```

**一日の終わり:**

```
あなた: "wrap up"
# → すべてのノートにリンクがあるか確認
# → インデックスを更新
# → 改善点を提案
```

---

## ⚙️ 仕組み

**フォルダは目的別にグループ化。リンクは意味別にグループ化。** ノートは1つのフォルダ（その居場所）に存在しますが、多くのノート（そのコンテキスト）にリンクします。Claudeがこのグラフを維持し、作業ノートをプロジェクト、意思決定、人物に自動的にリンクします。リンクのないノートはバグです。

**プロジェクト中心の構成。** 各Railsアプリは`work/projects/`配下に独自のフォルダを持ち、README（リポジトリURL、デプロイ先、技術スタック、ステークホルダー、コンプライアンスメモ）、`decisions/`フォルダ（ADR用）、`notes/`フォルダ（作業ノート用）で構成されます。`/context-switch`を実行すると、Claudeはプロジェクトフォルダ全体を読み込んでコンテキストを復元します。

**ボールトファーストのメモリ**がセッション間・マシン間でコンテキストを保持します。永続的な知識はすべて`brain/`のトピックノート（git管理、Obsidianで閲覧可能、リンク付き）に保存されます。Claude Codeの`MEMORY.md`（`~/.claude/`）はボールト内の場所を指す自動読み込みインデックスであり、ストレージそのものではありません。これにより、記憶はマシン変更後も生き残り、グラフの一部として機能します。

**セッションには設計されたライフサイクルがあります。** `SessionStart`フックが自動的にNorth Starの目標、アクティブプロジェクト、最近の変更、未完了タスク、ボールト全体のファイル一覧を注入します — Claudeは白紙からではなく、コンテキストを持ってセッションを開始します。終了時に「wrap up」と言えば、Claudeが`/wrap-up`を実行 — ノートの検証、インデックスの更新、ギャップの検出を行います。`CLAUDE.md`がその間のすべてを統制します：ファイルの配置場所、リンクの仕方、ノートの分割タイミング、意思決定やデプロイの扱い方。

### フック

5つのライフサイクルフックが自動的にルーティングを処理します：

| フック | タイミング | 内容 |
|------|------|------|
| 🚀 SessionStart | 起動/再開時 | QMD再インデックス、North Star・プロジェクト・最近の変更・タスク・ファイル一覧を注入 |
| 💬 UserPromptSubmit | 全メッセージ | コンテンツを分類（意思決定、実績、アーキテクチャ、人物、プロジェクト、デプロイ、コンプライアンス）してルーティングヒントを注入 |
| ✍️ PostToolUse | `.md`書き込み後 | フロントマターの検証、ウィキリンクの確認、フォルダ配置の検証 |
| 💾 PreCompact | コンテキスト圧縮前 | セッション記録を`thinking/session-logs/`にバックアップ |
| 🏁 Stop | セッション終了時 | チェックリスト：完了プロジェクトのアーカイブ、インデックス更新、孤立ノートの確認 |

> [!TIP]
> ただ話すだけ。フックがルーティングを処理します。

---

## 📅 日常ワークフロー

**朝**: `/standup`を実行。ClaudeがNorth Star、アクティブプロジェクト、未完了タスク、最近の変更を読み込みます。構造化されたサマリーと優先度の提案が表示されます。

**プロジェクト切り替え**: `/context-switch <project>`を実行。ClaudeがプロジェクトREADME、直近のノート、未解決の意思決定、関連するリファレンス資料を読み込みます。複数プロジェクトを管理する上で最も重要なコマンドです。

**日中**: 自然に話しましょう。下した決定、実行中のデプロイ、コンプライアンスの問題を伝えてください。分類フックがClaudeに各情報を正しく整理するよう促します。まとめてダンプしたい場合は`/dump`を使い、すべてを一度に語ってください。

**終業時**: 「wrap up」と言えば、Claudeが`/wrap-up`を呼び出します — ノートの検証、インデックスの更新、リンクの確認を行います。

**週次**: `/weekly`を実行してプロジェクト横断の振り返り — North Starとの整合性確認、パターンの発見、記録漏れの実績、翌週の優先事項。`/vault-audit`を実行して孤立ノート、壊れたリンク、古くなったコンテンツを検出します。

---

## 🛠️ コマンド

`.claude/commands/`で定義されています。任意のClaude Codeセッションで実行できます。

| コマンド | 機能 |
|---------|------|
| `/standup` | 朝のキックオフ — コンテキスト読み込み、前日の振り返り、タスクの表示、優先度の提案 |
| `/dump` | フリーフォームキャプチャ — 何でも自然に話せば、Claudeが適切なノートに振り分け |
| `/wrap-up` | セッション全体のレビュー — ノート、インデックス、リンクの検証、改善点の提案 |
| `/humanize` | 文体の調整 — Claudeが書いたテキストをあなたが書いたように修正 |
| `/weekly` | 週次振り返り — プロジェクト横断のパターン、North Starとの整合性、記録漏れの実績 |
| `/weekly-review` | 軽量なプロジェクト横断レビュー — 完了した作業、停滞中の作業、Index.mdの更新 |
| `/context-switch` | プロジェクトのコンテキスト再読み込み — README、直近のノート、未解決の意思決定 |
| `/project-status` | 単一プロジェクトの詳細ステータス確認 — ノート、意思決定、古い項目、GitHubイシュー |
| `/issue-capture` | GitHubイシューURLから作業ノートを生成（フロントマター自動入力） |
| `/decision` | 適切なプロジェクトの`decisions/`フォルダにADRを自動採番で作成 |
| `/deploy-checklist` | デプロイ手順書を呼び出し、デプロイ前後のチェックを順に実施 |
| `/project-archive` | 完了プロジェクトを`work/projects/`から`work/archive/`に移動し、インデックスを更新 |
| `/vault-audit` | インデックス、リンク、孤立ノート、古いコンテキストを監査 |
| `/vault-upgrade` | 既存ボールトからコンテンツをインポート — バージョン検出、分類、移行 |

---

## 🤖 サブエージェント

分離されたコンテキストウィンドウで実行される専門エージェント。メインの会話を汚さずに重い処理を担当します。

| エージェント | 目的 | 呼び出し元 |
|------------|------|------------|
| `context-loader` | 人物、プロジェクト、コンセプトに関するボールトコンテキストをすべて読み込み | 直接呼び出し |
| `cross-linker` | 不足しているウィキリンク、孤立ノート、壊れたバックリンクを発見 | `/vault-audit` |
| `vault-librarian` | ボールトの徹底メンテナンス — 孤立ノート、壊れたリンク、古いノート | `/vault-audit` |
| `vault-migrator` | ソースボールトからコンテンツを分類、変換、移行 | `/vault-upgrade` |

> [!NOTE]
> サブエージェントは`.claude/agents/`で定義されています。ドメイン固有のワークフロー用に独自のエージェントを追加できます。

---

## 📋 Bases

`bases/`フォルダには、ノートのフロントマタープロパティをクエリするデータベースビューが格納されています。ノートが変更されると自動的に更新されます。

| Base | 表示内容 |
|------|---------|
| Projects | 全プロジェクトREADME（ステータス、Railsバージョン、最終更新日付き） |
| Work Dashboard | プロジェクト別にグループ化されたアクティブな作業ノート |
| People Directory | `org/people/`の全員（役割、チーム付き） |
| Templates | 全テンプレートへのクイックアクセス |

`Home.md`がこれらのビューを埋め込んでおり、ボールトのダッシュボードとして機能します。

---

## 🔄 アップグレード

obsidian-mindの古いバージョン（または任意のObsidianボールト）をお使いですか？`/vault-upgrade`コマンドでコンテンツを最新テンプレートに移行できます：

```bash
# 1. 最新のobsidian-mindをクローン
git clone https://github.com/breferrari/obsidian-mind.git ~/new-vault

# 2. Claude Codeで開く
cd ~/new-vault && claude

# 3. 古いボールトを指定してアップグレードを実行
/vault-upgrade ~/my-old-vault
```

Claudeが以下を行います：
1. **検出** — ボールトのバージョンを特定（v1〜v3.3、またはobsidian-mind以外のボールトとして識別）
2. **棚卸し** — すべてのファイルを分類（ユーザーコンテンツ、スキャフォールド、インフラ、未分類）
3. **移行プランの提示** — コピー、変換、スキップされるものを正確に確認できます
4. **承認後に実行** — フロントマターの変換、ウィキリンクの修正、インデックスの再構築
5. **検証** — 孤立ノート、壊れたリンク、不足しているフロントマターをチェック

古いボールトは**一切変更されません**。`--dry-run`を使えば、実行せずにプランだけをプレビューできます。

> [!NOTE]
> obsidian-mindだけでなく、あらゆるObsidianボールトで動作します。obsidian-mind以外のボールトの場合、Claudeは各ノートを読んで意味的に分類し、作業ノート、人物、意思決定、リファレンス資料を適切なフォルダに振り分けます。

---

## 🚀 クイックスタート

1. このリポジトリをクローン（または**GitHubテンプレート**として使用）
2. フォルダを**Obsidianボールト**として開く
3. 設定 → 一般で**Obsidian CLI**を有効化（Obsidian 1.12以上が必要）
4. ボールトディレクトリで**`claude`**を実行
5. **`brain/North Star.md`**に目標を記入 — これがすべてのセッションの基盤になります
6. `work/projects/`にProject READMEテンプレートを使って最初のプロジェクトフォルダを作成
7. 仕事について話し始める

### オプション：QMDセマンティック検索

ボールト全体のセマンティック検索（ノートのタイトルが「Redis Migration ADR」でも「キャッシュについて何を決めた？」で見つかる）：

```bash
npm install -g @tobilu/qmd
qmd collection add . --name vault --mask "**/*.md"
qmd context add qmd://vault "Developer's work vault: projects, decisions, deploys, compliance, people"
qmd update && qmd embed
```

> [!NOTE]
> QMDがインストールされていなくても、すべて動作します — ClaudeはObsidian CLIとgrepにフォールバックします。

---

## 📁 ボールト構造

```
Home.md                 ボールトのエントリーポイント — 埋め込みBaseビュー、クイックリンク
CLAUDE.md               運用マニュアル — Claudeが毎セッション読み込み
vault-manifest.json     テンプレートメタデータ — バージョン、構造、スキーマ
CHANGELOG.md            バージョン履歴
CONTRIBUTING.md         テンプレート開発チェックリスト
README.md               プロダクトドキュメント
LICENSE                 MITライセンス

bases/                  動的データベースビュー（Projects、Work Dashboard、People、Templates）

work/
  projects/
    <project-name>/     Railsアプリごとに1フォルダ
      README.md         プロジェクトコンテキスト：リポジトリ、デプロイ先、技術スタック、ステークホルダー、コンプライアンス
      decisions/        このプロジェクトにスコープされたADR
      notes/            このプロジェクトの日付付き作業ノート
  archive/<name>/       完了/終了したプロジェクトフォルダ
  Index.md              全作業のMap of Content

org/
  people/               人物ごとに1ノート — PI、IT担当者、コラボレーター
  teams/                チームごとに1ノート — メンバー、スコープ
  People & Context.md   組織知識のMOC

perf/
  Brag Doc.md           実績の継続記録（作業ノートへのリンク付き）

brain/
  North Star.md         目標とフォーカスエリア — 毎セッション読み込み
  Memories.md           記憶トピックのインデックス
  Key Decisions.md      重要な意思決定とその理由
  Patterns.md           作業全体で観察された繰り返しパターン
  Gotchas.md            うまくいかなかったこととその理由
  Skills.md             カスタムワークフローとスラッシュコマンド

reference/
  compliance/           HIPAA、IRB、規制関連ノート
  ops/                  デプロイ手順書と運用手順
  infrastructure/       ネットワーク、サーバー、環境関連ノート
thinking/               ドラフト用スクラッチパッド — 知見を昇格させたら削除
templates/              YAMLフロントマター付きObsidianテンプレート

.claude/
  commands/             14個のスラッシュコマンド
  agents/               4個のサブエージェント
  scripts/              フックスクリプト
  skills/               Obsidian + QMDスキル
  settings.json         5つのフック設定
```

---

## 📝 テンプレート

YAMLフロントマター付きテンプレート。段階的開示のための`description`フィールドを含みます：

- **Work Note** — date、description、project、github_issue、status、tags
- **Decision Record** — date、description、project、status（proposed/accepted/deprecated）、context
- **Thinking Note** — date、description、context、tags（スクラッチパッド — 昇格後に削除）
- **Project README** — date、description、project、status、rails_version、ruby_version、stakeholders、compliance

---

## 🔧 同梱内容

### Obsidianスキル

[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)が`.claude/skills/`にプリインストール済み：

- **obsidian-markdown** — Obsidianフレーバーのmarkdown（ウィキリンク、埋め込み、コールアウト、プロパティ）
- **obsidian-cli** — ボールト操作用CLIコマンド
- **obsidian-bases** — データベーススタイルの`.base`ファイル
- **json-canvas** — ビジュアル`.canvas`ファイル作成
- **defuddle** — WebページからMarkdownへの変換

### QMDスキル

`.claude/skills/qmd/`にあるカスタムスキル。Claudeに[QMD](https://github.com/tobi/qmd)セマンティック検索を積極的に活用するよう教えます — ファイルを読む前、ノートを作成する前（重複チェック）、ノートを作成した後（リンクすべき関連コンテンツの発見）に使用します。

---

## 🎨 カスタマイズ

これは出発点です。あなたの働き方に合わせて適応させてください：

| 対象 | 場所 |
|------|------|
| あなたの目標 | `brain/North Star.md` — すべてのセッションの基盤 |
| あなたのプロジェクト | `work/projects/` — アプリごとに1フォルダ（README付き） |
| あなたの連絡先 | `org/` — PI、IT担当者、コラボレーターを追加 |
| あなたのコンプライアンス | `reference/compliance/` — HIPAA、IRB、監査要件 |
| あなたの手順書 | `reference/ops/` — プロジェクトごとのデプロイ手順 |
| あなたのツール | `.claude/commands/` — GitHub orgに合わせて編集 |
| あなたの規約 | `CLAUDE.md` — 運用マニュアル、使いながら進化させる |
| あなたのドメイン | フォルダの追加、`.claude/agents/`へのサブエージェント追加、`.claude/scripts/`への分類ルール追加 |

> [!IMPORTANT]
> `CLAUDE.md`は運用マニュアルです。規約を変更したら更新してください — Claudeは毎セッション読み込みます。

---

## 📋 要件

- [Obsidian](https://obsidian.md) 1.12以上（CLIサポートのため）
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- Python 3（フックスクリプト用）
- Git（バージョン履歴用）
- [QMD](https://github.com/tobi/qmd)（オプション、セマンティック検索用）

---

## 🙏 設計上の影響を受けたもの

- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) — 公式Obsidianエージェントスキル
- [James Bedford](https://x.com/jameesy) — ボールト構造の哲学、AI生成コンテンツの分離
- [arscontexta](https://github.com/agenticnotetaking/arscontexta) — descriptionフィールドによる段階的開示、セッションフック

---

## 📄 ライセンス

MIT
