const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  generateStream: (data) => ipcRenderer.invoke('llm-generate-stream', data),
  onLLMToken: (callback) => ipcRenderer.on('llm-token', (_event, value) => callback(value)),
  onLLMDone: (callback) => ipcRenderer.on('llm-done', (_event, value) => callback(value)),
  removeLLMListeners: () => {
    ipcRenderer.removeAllListeners('llm-token');
    ipcRenderer.removeAllListeners('llm-done');
  }
});
