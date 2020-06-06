from typing import List


class FromShortestSolution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        pass


class FinalSolution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


if __name__ == '__main__':
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    expected = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    output = FinalSolution().reconstructQueue(people)
    print(output)
    print(output == expected)
