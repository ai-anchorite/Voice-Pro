module.exports = {
  daemon: true,
  run: [
    {
      method: "shell.run",
      params: {
        venv: "env",
        path: "app",
        env: {
          GRADIO_SERVER_PORT: "{{port}}"
        },
        message: [
          "python -u start-voice.py",
        ],
        on: [{
          event: "/error/i",
          break: false
        }, {
          event: "/Running on.*?(http:\\/\\/\\S+)/",
          done: true
        }]
      }
    },
    {
      method: "local.set",
      params: {
        url: "{{input.event[1]}}"
      }
    }
  ]
}
