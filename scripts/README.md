# YouTube Thumbnail Fetcher

YouTubeの動画URLからサムネイル画像を自動取得し、カバーイメージとして使用できるスクリプトです。

## 機能

- YouTubeのURLから動画IDを自動抽出
- 最高品質のサムネイル画像を自動ダウンロード
- 複数の品質レベルに対応（maxresdefault → sddefault → hqdefault → mqdefault → default）
- ローカルファイルとして保存、またはURLのみ取得

## 使用方法

### 基本的な使い方

```bash
# URLのみ指定（video_id.jpgとして保存）
python3 scripts/youtube_thumbnail.py https://youtu.be/0fHb1DeYvCQ

# 出力ファイル名を指定
python3 scripts/youtube_thumbnail.py https://youtu.be/0fHb1DeYvCQ cover.jpg

# static/coversディレクトリに保存
python3 scripts/youtube_thumbnail.py https://youtu.be/0fHb1DeYvCQ static/covers/my-song.jpg
```

### サポートされているURL形式

- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`

## 実例

### 例1: ローカルファイルとして保存

```bash
python3 scripts/youtube_thumbnail.py https://youtu.be/0fHb1DeYvCQ static/covers/bohemian-rhapsody.jpg
```

出力:
```
Processing URL: https://youtu.be/0fHb1DeYvCQ
Video ID: 0fHb1DeYvCQ
Trying to download maxresdefault quality from: https://img.youtube.com/vi/0fHb1DeYvCQ/maxresdefault.jpg
✓ Successfully downloaded thumbnail: static/covers/bohemian-rhapsody.jpg
  Quality: maxresdefault
  URL: https://img.youtube.com/vi/0fHb1DeYvCQ/maxresdefault.jpg

✓ Thumbnail URL for markdown:
  cover_image = "https://img.youtube.com/vi/0fHb1DeYvCQ/maxresdefault.jpg"
```

### 例2: Markdownファイルでの使用

スクリプトの出力から、`cover_image`の値をコピーしてMarkdownファイルに追加：

```markdown
+++
title = "Bohemian Rhapsody - Queen"
date = 2026-05-22
[extra]
artist = "Queen"
genre = "Progressive Rock"
year = "1975"
cover_image = "https://img.youtube.com/vi/0fHb1DeYvCQ/maxresdefault.jpg"
youtube_embed = "https://www.youtube.com/embed/0fHb1DeYvCQ"
+++
```

## サムネイル品質について

スクリプトは以下の順序で品質を試行します：

1. **maxresdefault** (1280x720) - 最高品質、すべての動画で利用可能とは限らない
2. **sddefault** (640x480) - 標準品質
3. **hqdefault** (480x360) - 高品質
4. **mqdefault** (320x180) - 中品質
5. **default** (120x90) - 最低品質

最初に利用可能な品質が自動的に選択されます。

## ローカル保存 vs URL直接指定

### ローカル保存の利点
- サイトの読み込み速度が向上
- YouTubeのサーバーに依存しない
- 画像の編集・加工が可能

### URL直接指定の利点
- ストレージ容量を節約
- 常に最新のサムネイルを表示
- 設定が簡単

## トラブルシューティング

### エラー: "Could not extract video ID from URL"

URLの形式が正しいか確認してください。サポートされている形式は上記を参照。

### エラー: "Failed to download thumbnail in any quality"

- インターネット接続を確認
- 動画IDが正しいか確認
- 動画が削除されていないか確認

## Pythonモジュールとしての使用

```python
from scripts.youtube_thumbnail import extract_video_id, get_thumbnail_url, download_thumbnail

# 動画IDを抽出
video_id = extract_video_id("https://youtu.be/0fHb1DeYvCQ")
print(video_id)  # 0fHb1DeYvCQ

# サムネイルURLを取得
url = get_thumbnail_url(video_id)
print(url)  # https://img.youtube.com/vi/0fHb1DeYvCQ/maxresdefault.jpg

# サムネイルをダウンロード
download_thumbnail(video_id, "output.jpg")
```

## ライセンス

このスクリプトは自由に使用・改変できます。