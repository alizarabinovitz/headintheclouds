# **Head in the Sky**

A project for data visualization. By Laurena Huh and Aliza Rabinovitz. HackMIT 2022.

## Data Insights from the description

Here is a little information about the data structure.

Schema:

```ts
type EventName =
  | "ping"
  | "hand_held"
  | "chat_msg"
  | "wingbuff_collect"
  | "wingbuff_drop"
  | "candle_purchased"
  | "spirit_shop_item_purchased"
  | "got_wax"
  | "healed_player";
type SkyEvent = {
  time: number;
  userId: number;
  platform: "android" | "iphoneos" | "nx" | "huawei";
  pos: [number, number, number];
  fps: number;
  event: Record<EventName, number>;
};
```

## Key Descriptions

| Event Name | Description                                                                              |
| ---------- | ---------------------------------------------------------------------------------------- |
| time       | millisecond timestamp when the event was recorded                                                 |
| userId     | unique identifier given to each user                                                     |
| platform   | the type of device used to play the game. We are cross platform. `nx` is nintendo switch |
| country    | country code for the ip address the user is using                                        |
| events     | hash map of events that have occurred within the last 5 seconds for that user.           |


### Event Name Descriptions

| Event Name                 | Description                                                                                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ping                       | Pings are generated whenever the two conditions happen first: minimum distance of 10 units or a minimum time of 30 seconds between pings. Pings will only be sent when the app is in the front. |
| hand_held                  | When a player holds the hand of another player or NPC - not triggered by the handhold leader, only followers                                                                                    |
| chat_msg                   | When a chat message is sent by the local player                                                                                                                                                 |
| wingbuff_collect           | When a wing buff is picked up (shiny boy)                                                                                                                                                       |
| wingbuff_drop              | drop wing buff due to damage                                                                                                                                                                    |
| candle_purchased           | triggered by in app purchase                                                                                                                                                                    |
| spirit_shop_item_purchased | purchase with in game currency                                                                                                                                                                  |
| got_wax                    | in game currency pickup                                                                                                                                                                         |
| healed_player              | when the player the user chose to heal is healed to the point of standing up                                                                                                                    |

