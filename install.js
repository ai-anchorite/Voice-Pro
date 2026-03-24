module.exports = {
  run: [

    {
      method: "shell.run",
      params: {
        venv: "env",
        path: "app",
        message: [
          "uv pip install -r requirements.txt"
        ]
      }
    },

    {
      method: "shell.run",
      params: {
        path: "app",
        message: [
          "conda install -y cudnn=8.9.2.26 -c anaconda --no-update-deps"
        ]
      }
    },

    {
      method: "script.start",
      params: {
        uri: "torch.js",
        params: {
          venv: "env",
          path: "app",
          // flashattention: true,   // uncomment this line if your project requires flashattention
          // xformers: true,   // uncomment this line if your project requires xformers
          // triton: true,   // uncomment this line if your project requires triton
          // sageattention: true   // uncomment this line if your project requires sageattention
        }
      }
    },
  ]
}
