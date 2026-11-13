## bug1.py
**AI Explanation:** The slice `items[len(items) - n - 1]` includes one extra item.
**Suggested Fix:** Use `items[len(items) - n:]`.
**Confidence:** High
