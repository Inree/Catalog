class EntriesFinder:

    @staticmethod
    def findEntries(entries, query):
        for entry in entries:
            if entry.fits(query):
                yield entry

    @staticmethod
    def findEntryByEmail(entries, email):
        for entry in entries:
            if entry.email == email:
                return entry
        return None
