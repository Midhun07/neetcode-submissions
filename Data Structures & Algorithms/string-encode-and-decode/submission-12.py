class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = '<br#>'.join(strs) if len(strs) > 0 else "empty"
        return encoded_str
    def decode(self, s: str) -> List[str]:
        s_list = s.split('<br#>') if s != "empty" else []
        return s_list