# test_manual_preview.py
import shutil
import os
import unittest
import sys

sys.path.append("..")
from src.manga import manga_config
from src.manga import manga_preview


class TestManualPreview(unittest.TestCase):

    def setUp(self):
        manga_config.SOURCE_PATH = "./tests/data/test_preview/src/"
        manga_config.DESTINATION_PATH = "./tests/data/test_preview/dest/"
        os.mkdir("./tests/data/test_preview/dest/")

    def tearDown(self):
        try:
            shutil.rmtree("./tests/data/test_preview/dest/")
            shutil.rmtree("./tests/data/test_preview/src/")
        except:
            pass

    def test_single_chapter(self):
        shutil.copytree("./tests/data/test_preview/manual_single_chapter/src/", manga_config.SOURCE_PATH)
        result = manga_preview.manual_single_chapter_preview("Blue Box", 6, "Good Manga")
        expected_result = ['Rename: 01.jpg to Blue Box - CH006PG01 - Good Manga.jpg', 'Rename: 02.jpg to Blue Box - CH006PG02 - Good Manga.jpg', 'Rename: 04.jpg to Blue Box - CH006PG03 - Good Manga.jpg', 'Rename: 05.jpg to Blue Box - CH006PG04 - Good Manga.jpg', 'Rename: 06.jpg to Blue Box - CH006PG05 - Good Manga.jpg', 'Rename: 07.jpg to Blue Box - CH006PG06 - Good Manga.jpg', 'Rename: 08.jpg to Blue Box - CH006PG07 - Good Manga.jpg', 'Rename: 09.jpg to Blue Box - CH006PG08 - Good Manga.jpg', 'Rename: 10.jpg to Blue Box - CH006PG09 - Good Manga.jpg', 'Rename: 11.jpg to Blue Box - CH006PG10 - Good Manga.jpg', 'Rename: 12.jpg to Blue Box - CH006PG11 - Good Manga.jpg', 'Rename: 13.jpg to Blue Box - CH006PG12 - Good Manga.jpg', 'Rename: 14.jpg to Blue Box - CH006PG13 - Good Manga.jpg', 'Rename: 15.jpg to Blue Box - CH006PG14 - Good Manga.jpg', 'Rename: 16.jpg to Blue Box - CH006PG15 - Good Manga.jpg', 'Rename: 17.jpg to Blue Box - CH006PG16 - Good Manga.jpg', 'Rename: 18.jpg to Blue Box - CH006PG17 - Good Manga.jpg']
        self.assertEqual(result, expected_result)
        shutil.rmtree(manga_config.SOURCE_PATH)

        shutil.copytree("./tests/data/test_preview/manual_single_chapter/src - multi/", manga_config.SOURCE_PATH)
        result = manga_preview.manual_multiple_chapter_preview("Naruto")
        expected_result = ['Rename: Attack on Titan - CH138PG01 - A Long Dream.jpg to Naruto - CH138PG01 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG02 - A Long Dream.jpg to Naruto - CH138PG02 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG03 - A Long Dream.jpg to Naruto - CH138PG03 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG04 - A Long Dream.jpg to Naruto - CH138PG04 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG05 - A Long Dream.jpg to Naruto - CH138PG05 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG06 - A Long Dream.jpg to Naruto - CH138PG06 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG07 - A Long Dream.jpg to Naruto - CH138PG07 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG08 - A Long Dream.jpg to Naruto - CH138PG08 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG09 - A Long Dream.jpg to Naruto - CH138PG09 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG10 - A Long Dream.jpg to Naruto - CH138PG10 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG11 - A Long Dream.jpg to Naruto - CH138PG11 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG12 - A Long Dream.jpg to Naruto - CH138PG12 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG13 - A Long Dream.jpg to Naruto - CH138PG13 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG14 - A Long Dream.jpg to Naruto - CH138PG14 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG15 - A Long Dream.jpg to Naruto - CH138PG15 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG16 - A Long Dream.jpg to Naruto - CH138PG16 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG17 - A Long Dream.jpg to Naruto - CH138PG17 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG18 - A Long Dream.jpg to Naruto - CH138PG18 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG19 - A Long Dream.jpg to Naruto - CH138PG19 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG20 - A Long Dream.jpg to Naruto - CH138PG20 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG21 - A Long Dream.jpg to Naruto - CH138PG21 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG22 - A Long Dream.jpg to Naruto - CH138PG22 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG23 - A Long Dream.jpg to Naruto - CH138PG23 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG24 - A Long Dream.jpg to Naruto - CH138PG24 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG25 - A Long Dream.jpg to Naruto - CH138PG25 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG26 - A Long Dream.jpg to Naruto - CH138PG26 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG27 - A Long Dream.jpg to Naruto - CH138PG27 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG28 - A Long Dream.jpg to Naruto - CH138PG28 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG29 - A Long Dream.jpg to Naruto - CH138PG29 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG30 - A Long Dream.jpg to Naruto - CH138PG30 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG31 - A Long Dream.jpg to Naruto - CH138PG31 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG32 - A Long Dream.jpg to Naruto - CH138PG32 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG33 - A Long Dream.jpg to Naruto - CH138PG33 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG34 - A Long Dream.jpg to Naruto - CH138PG34 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG35 - A Long Dream.jpg to Naruto - CH138PG35 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG36 - A Long Dream.jpg to Naruto - CH138PG36 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG37 - A Long Dream.jpg to Naruto - CH138PG37 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG38 - A Long Dream.jpg to Naruto - CH138PG38 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG39 - A Long Dream.jpg to Naruto - CH138PG39 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG40 - A Long Dream.jpg to Naruto - CH138PG40 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG41 - A Long Dream.jpg to Naruto - CH138PG41 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG42 - A Long Dream.jpg to Naruto - CH138PG42 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG43 - A Long Dream.jpg to Naruto - CH138PG43 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG44 - A Long Dream.jpg to Naruto - CH138PG44 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG45 - A Long Dream.jpg to Naruto - CH138PG45 - Single Chapter.jpg', 'Rename: Attack on Titan - CH138PG46 - A Long Dream.jpg to Naruto - CH138PG46 - Single Chapter.jpg']
        self.assertEqual(result, expected_result)

    def test_multi_chapter(self):
        shutil.copytree("./tests/data/test_preview/manual_multi_chapter/src/", manga_config.SOURCE_PATH)
        result = manga_preview.manual_multiple_chapter_preview("Bleach")
        expected_result = ['Rename: Attack on Titan - CH137PG01 - Titans.jpeg to Bleach - CH001PG01 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG02 - Titans.jpeg to Bleach - CH001PG02 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG03 - Titans.jpeg to Bleach - CH001PG03 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG04 - Titans.jpeg to Bleach - CH001PG04 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG05 - Titans.jpeg to Bleach - CH001PG05 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG06 - Titans.jpeg to Bleach - CH001PG06 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG07 - Titans.jpeg to Bleach - CH001PG07 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG08 - Titans.jpeg to Bleach - CH001PG08 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG09 - Titans.jpeg to Bleach - CH001PG09 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG10 - Titans.jpeg to Bleach - CH001PG10 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG11 - Titans.jpeg to Bleach - CH001PG11 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG12 - Titans.jpeg to Bleach - CH001PG12 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG13 - Titans.jpeg to Bleach - CH001PG13 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG14 - Titans.jpeg to Bleach - CH001PG14 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG15 - Titans.jpeg to Bleach - CH001PG15 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG16 - Titans.jpeg to Bleach - CH001PG16 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG17 - Titans.jpeg to Bleach - CH001PG17 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG18 - Titans.jpeg to Bleach - CH001PG18 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG19 - Titans.jpeg to Bleach - CH001PG19 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG20 - Titans.jpeg to Bleach - CH001PG20 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG21 - Titans.jpeg to Bleach - CH001PG21 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG22 - Titans.jpeg to Bleach - CH001PG22 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG23 - Titans.jpeg to Bleach - CH001PG23 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG24 - Titans.jpeg to Bleach - CH001PG24 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG25 - Titans.jpeg to Bleach - CH001PG25 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG26 - Titans.jpeg to Bleach - CH001PG26 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG27 - Titans.jpeg to Bleach - CH001PG27 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG28 - Titans.jpeg to Bleach - CH001PG28 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG29 - Titans.jpeg to Bleach - CH001PG29 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG30 - Titans.jpeg to Bleach - CH001PG30 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG31 - Titans.jpeg to Bleach - CH001PG31 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG32 - Titans.jpeg to Bleach - CH001PG32 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG33 - Titans.jpeg to Bleach - CH001PG33 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG34 - Titans.jpeg to Bleach - CH001PG34 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG35 - Titans.jpeg to Bleach - CH001PG35 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG36 - Titans.jpeg to Bleach - CH001PG36 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG37 - Titans.jpeg to Bleach - CH001PG37 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG38 - Titans.jpeg to Bleach - CH001PG38 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG39 - Titans.jpeg to Bleach - CH001PG39 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG40 - Titans.jpeg to Bleach - CH001PG40 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG41 - Titans.jpeg to Bleach - CH001PG41 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG42 - Titans.jpeg to Bleach - CH001PG42 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG43 - Titans.jpeg to Bleach - CH001PG43 - New Series.jpeg', 'Rename: Attack on Titan - CH137PG44 - Titans.jpeg to Bleach - CH001PG44 - New Series.jpeg', 'Rename: Attack on Titan - CH138PG01 - A Long Dream.jpg to Bleach - CH133PG01 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG02 - A Long Dream.jpg to Bleach - CH133PG02 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG03 - A Long Dream.jpg to Bleach - CH133PG03 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG04 - A Long Dream.jpg to Bleach - CH133PG04 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG05 - A Long Dream.jpg to Bleach - CH133PG05 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG06 - A Long Dream.jpg to Bleach - CH133PG06 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG07 - A Long Dream.jpg to Bleach - CH133PG07 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG08 - A Long Dream.jpg to Bleach - CH133PG08 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG09 - A Long Dream.jpg to Bleach - CH133PG09 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG10 - A Long Dream.jpg to Bleach - CH133PG10 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG11 - A Long Dream.jpg to Bleach - CH133PG11 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG12 - A Long Dream.jpg to Bleach - CH133PG12 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG13 - A Long Dream.jpg to Bleach - CH133PG13 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG14 - A Long Dream.jpg to Bleach - CH133PG14 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG15 - A Long Dream.jpg to Bleach - CH133PG15 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG16 - A Long Dream.jpg to Bleach - CH133PG16 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG17 - A Long Dream.jpg to Bleach - CH133PG17 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG18 - A Long Dream.jpg to Bleach - CH133PG18 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG19 - A Long Dream.jpg to Bleach - CH133PG19 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG20 - A Long Dream.jpg to Bleach - CH133PG20 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG21 - A Long Dream.jpg to Bleach - CH133PG21 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG22 - A Long Dream.jpg to Bleach - CH133PG22 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG23 - A Long Dream.jpg to Bleach - CH133PG23 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG24 - A Long Dream.jpg to Bleach - CH133PG24 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG25 - A Long Dream.jpg to Bleach - CH133PG25 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG26 - A Long Dream.jpg to Bleach - CH133PG26 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG27 - A Long Dream.jpg to Bleach - CH133PG27 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG28 - A Long Dream.jpg to Bleach - CH133PG28 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG29 - A Long Dream.jpg to Bleach - CH133PG29 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG30 - A Long Dream.jpg to Bleach - CH133PG30 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG31 - A Long Dream.jpg to Bleach - CH133PG31 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG32 - A Long Dream.jpg to Bleach - CH133PG32 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG33 - A Long Dream.jpg to Bleach - CH133PG33 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG34 - A Long Dream.jpg to Bleach - CH133PG34 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG35 - A Long Dream.jpg to Bleach - CH133PG35 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG36 - A Long Dream.jpg to Bleach - CH133PG36 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG37 - A Long Dream.jpg to Bleach - CH133PG37 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG38 - A Long Dream.jpg to Bleach - CH133PG38 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG39 - A Long Dream.jpg to Bleach - CH133PG39 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG40 - A Long Dream.jpg to Bleach - CH133PG40 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG41 - A Long Dream.jpg to Bleach - CH133PG41 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG42 - A Long Dream.jpg to Bleach - CH133PG42 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG43 - A Long Dream.jpg to Bleach - CH133PG43 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG44 - A Long Dream.jpg to Bleach - CH133PG44 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG45 - A Long Dream.jpg to Bleach - CH133PG45 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH138PG46 - A Long Dream.jpg to Bleach - CH133PG46 - Battle of Heaven and Earth.jpg', 'Rename: Attack on Titan - CH136PG01 - Devote Your Hearts.jpg to Bleach - CH015PG01 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG02 - Devote Your Hearts.jpg to Bleach - CH015PG02 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG03 - Devote Your Hearts.jpg to Bleach - CH015PG03 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG04 - Devote Your Hearts.jpg to Bleach - CH015PG04 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG05 - Devote Your Hearts.jpg to Bleach - CH015PG05 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG06 - Devote Your Hearts.jpg to Bleach - CH015PG06 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG07 - Devote Your Hearts.jpg to Bleach - CH015PG07 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG08 - Devote Your Hearts.jpg to Bleach - CH015PG08 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG09 - Devote Your Hearts.jpg to Bleach - CH015PG09 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG10 - Devote Your Hearts.jpg to Bleach - CH015PG10 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG11 - Devote Your Hearts.jpg to Bleach - CH015PG11 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG12 - Devote Your Hearts.jpg to Bleach - CH015PG12 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG13 - Devote Your Hearts.jpg to Bleach - CH015PG13 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG14 - Devote Your Hearts.jpg to Bleach - CH015PG14 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG15 - Devote Your Hearts.jpg to Bleach - CH015PG15 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG16 - Devote Your Hearts.jpg to Bleach - CH015PG16 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG17 - Devote Your Hearts.jpg to Bleach - CH015PG17 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG18 - Devote Your Hearts.jpg to Bleach - CH015PG18 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG19 - Devote Your Hearts.jpg to Bleach - CH015PG19 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG20 - Devote Your Hearts.jpg to Bleach - CH015PG20 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG21 - Devote Your Hearts.jpg to Bleach - CH015PG21 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG22 - Devote Your Hearts.jpg to Bleach - CH015PG22 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG23 - Devote Your Hearts.jpg to Bleach - CH015PG23 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG24 - Devote Your Hearts.jpg to Bleach - CH015PG24 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG25 - Devote Your Hearts.jpg to Bleach - CH015PG25 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG26 - Devote Your Hearts.jpg to Bleach - CH015PG26 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG27 - Devote Your Hearts.jpg to Bleach - CH015PG27 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG28 - Devote Your Hearts.jpg to Bleach - CH015PG28 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG29 - Devote Your Hearts.jpg to Bleach - CH015PG29 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG30 - Devote Your Hearts.jpg to Bleach - CH015PG30 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG31 - Devote Your Hearts.jpg to Bleach - CH015PG31 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG32 - Devote Your Hearts.jpg to Bleach - CH015PG32 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG33 - Devote Your Hearts.jpg to Bleach - CH015PG33 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG34 - Devote Your Hearts.jpg to Bleach - CH015PG34 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG35 - Devote Your Hearts.jpg to Bleach - CH015PG35 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG36 - Devote Your Hearts.jpg to Bleach - CH015PG36 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG37 - Devote Your Hearts.jpg to Bleach - CH015PG37 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG38 - Devote Your Hearts.jpg to Bleach - CH015PG38 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG39 - Devote Your Hearts.jpg to Bleach - CH015PG39 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG40 - Devote Your Hearts.jpg to Bleach - CH015PG40 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG41 - Devote Your Hearts.jpg to Bleach - CH015PG41 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG42 - Devote Your Hearts.jpg to Bleach - CH015PG42 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG43 - Devote Your Hearts.jpg to Bleach - CH015PG43 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG44 - Devote Your Hearts.jpg to Bleach - CH015PG44 - Kinda Cool.jpg', 'Rename: Attack on Titan - CH136PG45 - Devote Your Hearts.jpg to Bleach - CH015PG45 - Kinda Cool.jpg']
        self.assertEqual(result, expected_result)

    def test_manual_volume(self):
        shutil.copytree("./tests/data/test_preview/manual_volume/src/", manga_config.SOURCE_PATH)
        result = manga_preview.manual_volume_preview("One Piece", 23, "Best Volume Ever!")
        expected_result = ['Rename: 100 - More Chapters/ to One Piece Volume 23 - Best Volume Ever!/', 'Rename: 101 - Almost/ to One Piece Volume 23 - Best Volume Ever!/', 'Rename: 102 - The End/ to One Piece Volume 23 - Best Volume Ever!/', 'Rename: 96 - New/ to One Piece Volume 23 - Best Volume Ever!/', 'Rename: 97 - Chapter for/ to One Piece Volume 23 - Best Volume Ever!/', 'Rename: 98 - The Volume/ to One Piece Volume 23 - Best Volume Ever!/', 'Rename: 99 - Title Here/ to One Piece Volume 23 - Best Volume Ever!/']
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
