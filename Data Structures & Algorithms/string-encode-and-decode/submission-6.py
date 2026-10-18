class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "ITSATRAPABORTABORTABORT!!!"
        return "112358132134".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "ITSATRAPABORTABORTABORT!!!":
            return []
        return s.split("112358132134")