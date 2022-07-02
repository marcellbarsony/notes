# VSCodium Marketplace

You can switch and use the VS Code marketplace by using the following solutions.
However, note that it is not clear [whether this is legal](https://github.com/microsoft/vscode/issues/31168).

With the following environment variables:

  - `VSCODE_GALLERY_SERVICE_URL='https://marketplace.visualstudio.com/_apis/public/gallery'`
  - `VSCODE_GALLERY_CACHE_URL='https://vscode.blob.core.windows.net/gallery/index'`
  - `VSCODE_GALLERY_ITEM_URL='https://marketplace.visualstudio.com/items'`
  - `VSCODE_GALLERY_CONTROL_URL=''`
  - `VSCODE_GALLERY_RECOMMENDATIONS_URL=''`

Or by creating a custom product.json at the following location:

  - Windows: `%APPDATA%\VSCodium` or `%USERPROFILE%\AppData\Roaming\VSCodium`
  - macOS: `~/Library/Application Support/VSCodium`
  - Linux: `$XDG_CONFIG_HOME/VSCodium` or `~/.config/VSCodium`

with the content:

```json
{
  "extensionsGallery": {
    "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
    "cacheUrl": "https://vscode.blob.core.windows.net/gallery/index",
    "itemUrl": "https://marketplace.visualstudio.com/items",
    "controlUrl": "",
    "recommendationsUrl": ""
  }
}
```
