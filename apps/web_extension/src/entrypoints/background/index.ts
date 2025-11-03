import { onMessage } from "webext-bridge/background";

async function getDefinition({
  data,
}: {
  data: { word: string; context: string };
}): Promise<{ word: string; definitions: [{ definition: string }] }> {
  const word = data.word;
  const context = data.context;

  const response = await fetch("http://localhost:8000/definitions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ word: word, context: context }),
  });

  const result = await response.json();
  return result;
}

export default defineBackground(() => {
  onMessage("definitions:get", getDefinition);
});
