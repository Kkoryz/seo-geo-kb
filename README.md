# seo-geo-kb

这是一个用于 SEO/GEO 知识库的源码仓库（原始 Markdown 引用材料和索引构建脚本）。

重要说明
- 请不要将生成的 `.kb_index/` 或大体积 ZIP 文件提交到 Git（已在 `.gitignore` 中排除）。
- 当前 clean 版源码仓库是 `Kkoryz/seo-geo-kb`。`index-build-20260623` release 里保存了可直接还原的构建索引。

## 快速恢复已构建索引

如果只是要在新机器或 droplet 上使用知识库，优先下载 release 里的索引包，而不是重新跑嵌入模型。

```bash
cd /root/seo-geo-kb

# 下载已构建索引
mkdir -p /root/downloads
curl -fL \
  "https://github.com/Kkoryz/seo-geo-kb/releases/download/index-build-20260623/seo-geo-kb-index.zip" \
  -o /root/downloads/seo-geo-kb-index.zip

# 还原 .kb_index/
rm -rf .kb_index
unzip -oq /root/downloads/seo-geo-kb-index.zip -d /root/seo-geo-kb

# 验证 LanceDB 表
.venv/bin/python - <<'PY'
import lancedb
db = lancedb.connect("/root/seo-geo-kb/.kb_index")
table = db.open_table("seo_geo")
print("tables:", db.list_tables())
print("rows:", table.count_rows())
print("schema:", table.schema)
PY
```

期望结果：表名包含 `seo_geo`，当前索引约 `31,433` 条 chunk。

## 创建检索环境

```bash
cd /root/seo-geo-kb
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
```

首次运行检索时，如果本机还没有缓存 `BAAI/bge-m3` 和 `BAAI/bge-reranker-v2-m3`，需要临时允许 HuggingFace 联网下载模型：

```bash
HF_HUB_OFFLINE=0 TRANSFORMERS_OFFLINE=0 \
  .venv/bin/python search.py "schema markup for ecommerce product pages" --json -k 8
```

模型缓存好之后，可以直接离线检索：

```bash
.venv/bin/python search.py "internal linking SEO best practices" --json -k 8
```

## 从源码重建 `.kb_index`

前提
- 推荐 Python 3.10+
- 需要网络以下载嵌入/重排模型（示例中使用 `BAAI/bge-m3` 和 `BAAI/bge-reranker-v2-m3`）。

步骤（Linux/macOS 示例）

```bash
cd /root/seo-geo-kb

# 创建并激活虚拟环境（可选）
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

# 首次构建如果模型未缓存，需要临时允许联网
HF_HUB_OFFLINE=0 TRANSFORMERS_OFFLINE=0 \
  .venv/bin/python index_kb.py --max-chars 1800 --batch 16

# 成功后会生成 .kb_index/，此时可运行检索
.venv/bin/python search.py "你的查询文本" --json -k 8
```

步骤（Windows PowerShell 示例）

```powershell
# 进入项目目录
cd path\to\seo-geo-kb

# 创建并激活虚拟环境（可选）
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 安装依赖（或使用 requirements.txt）
pip install -r requirements.txt

# 首次构建如果模型未缓存，需要临时允许联网
$env:HF_HUB_OFFLINE="0"
$env:TRANSFORMERS_OFFLINE="0"
python index_kb.py --max-chars 1800 --batch 16

# 成功后会生成 .kb_index/，此时可运行检索
python search.py "你的查询文本" --json -k 8
```

注意事项
- 模型下载与推理可能需要较多内存或 GPU，若遇到问题请在更强的机器上跑或使用更小的模型。
- 若要分享已构建的索引（二进制）请使用 GitHub Releases、S3、Google Drive 或 Git LFS，不要直接把 `.kb_index/` 放入仓库。

常见问题
- 如果 `index_kb.py` 运行失败，请确保 `references/` 目录存在并包含 Markdown 源文件。

联系方式
- 如需我把索引上传到 Releases（zip），或用 LFS 配置远程，请告诉我。
