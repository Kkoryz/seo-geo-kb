# seo-geo-kb

这是一个用于 SEO/GEO 知识库的源码仓库（原始 Markdown 引用材料和索引构建脚本）。

重要说明
- 请不要将生成的 `.kb_index/` 或大体积 ZIP 文件提交到 Git（已在 `.gitignore` 中排除）。

如何重建 `.kb_index`

前提
- 推荐 Python 3.10+
- 需要网络以下载嵌入/重排模型（示例中使用 `BAAI/bge-m3` 和 `BAAI/bge-reranker-v2-m3`）。

步骤（PowerShell 示例）

```powershell
# 进入项目目录
cd path\to\seo-geo-kb

# 创建并激活虚拟环境（可选）
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 安装依赖（或使用 requirements.txt）
pip install -r requirements.txt

# 运行索引构建脚本（根据内存/速度调整参数）
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
