# Welcome to BulBul

A lightweight & powerful skill bot with multi end*point support.

## Commands

* `pip install *r requirements.dev.txt` * Install dependents.
* `sh ./scripts/docs*live.sh` * Star a live document.
* `sh ./scripts/lint.sh` * Run lint.

## Concepts

Here are the basic concepts, all pre-defined models saved in file `bulbul/builtins.py`.

* NLU
  * **PreProcessor**: Consume a `Query` object and return a `Query` object with
    processed text. Here is same examples:
    * remove while space.
    * convert emoji to token.
    * custom PreProcessor
  * **IntentTagger**: Consume a `Query` object and might return a list of `NLUResult`,
    each `NLUResult` contains a `Intent`.
  * **JointTagger**: Consume a `Query` object and might return a list of `NLUResult`,
    each `NLUResult` contains a `Intent` and a `Slot`.
  * **SlotTagger**: Consume a `NLUResult` object (which contain `Intent` object)
    and return a `NLUResult` (might contain a `Slot` obejct).

* **Skill**: Which consume a `NLUResult` object and return a optional `SkillResponse`
* **Plugin**
  * **RuleBasedPlugin** Which defines nlu rules and skill handler function in a single class.
* **Adapter**: Adapter will consume requests from different backend and convert it to
    a unified request for BulBul, and convert bulbuls response to json format required by
    different backends.

## Todo

* [ ] PreProcessor
  * [ ] WhiteSpaceRemover
  * [ ] EmojiConvertor

* [ ] RuleEngine
  * [ ] DictRule
  * [ ] RegexRule
  * [ ] Regex+DictRule
* [ ] ModelEngine
  * [ ] KerasModel
  * [ ] KashgariModel
* [ ] Skill
  * [ ] Weather
* [ ] Adapter
  * [ ] Wechaty
  * [ ] Telegram
  * [ ] Slack
