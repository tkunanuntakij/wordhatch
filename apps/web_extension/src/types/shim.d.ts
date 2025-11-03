import { ProtocolWithReturn } from "webext-bridge";

declare module "webext-bridge" {
  export interface ProtocolMap {
    "definitions:get": ProtocolWithReturn<
      { word: string; context: string },
      { word: string; definitions: [{ definition: string }] }
    >;
  }
}
