# Compatibility

| Capability | Requirement | Current claim |
|---|---|---|
| Text prompts | Host follows Markdown instructions | Portable design |
| Images | Host has vision and actual file access | Conditional |
| Video references | Video/frames/transcript access | Conditional; distinguish evidence types |
| Documentation lookup | Authorized browsing | Optional |
| Veo generation | External generator/service | Not implemented here |
| Duration, audio and reference controls | Confirmed provider/version documentation | Not assumed or tested |
| Files and script execution | Host filesystem/Python tools | Needed only for repository validation |

The prompt structure is not an official API schema. Do not guess flags, output sizes, frame rates, maximum durations or audio/lip-sync guarantees. Model/version capabilities can change. Verify current official documentation before technical integration; portable scene direction remains useful without such integration.
