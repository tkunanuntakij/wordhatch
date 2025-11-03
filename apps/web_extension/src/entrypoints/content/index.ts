import { sendMessage } from "webext-bridge/content-script";

async function mouseup_handler() {
  const selected = window.getSelection();
  const context = selected?.anchorNode?.parentNode?.textContent;
  const word = selected?.toString();
  if (!!word && !!context) {
    console.log({ word, context });
    const result = await sendMessage("definitions:get", { word, context }, "background");
    console.log("background result");
    console.log(result.word);
    console.log(result.definitions[0].definition);
  }
}

export default defineContentScript({
  matches: ["*://*/*"],
  main() {
    console.log("Hello content3.");
    document.addEventListener("dblclick", mouseup_handler);
  },
});
