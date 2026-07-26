class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for item in strs:
            encoded_str = encoded_str + '<bb#>' + item
        return encoded_str
    def decode(self, s: str) -> List[str]:
        print(s)
        s_list = s.strip().split('<bb#>')
        return s_list[1:]