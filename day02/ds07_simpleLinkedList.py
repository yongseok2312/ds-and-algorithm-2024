{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# file: ds07_simpleLinkedList.ipynb\n",
    "# desc: 단순 연결 리스트 일반 구현\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 자료구조 및 알고리즘\n",
    "\n",
    "- 단순연결리스트 일반 구현\n",
    "\n",
    "### 단순연결 리스트"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 초기화\n",
    "memory = []\n",
    "head, curr, prev = None, None, None\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Node():\n",
    "    # data, link 두개의 멤버변수 존재\n",
    "    # 생성자 추가\n",
    "    def __init__(self, name) -> None:\n",
    "        self.data = name\n",
    "        self.link = None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
