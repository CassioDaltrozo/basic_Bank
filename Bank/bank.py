from accounts import *
from people import *
from dataclasses import dataclass, field

@dataclass
class Bank:
    agencies : list[int] = field(default_factory=list[int])
    accounts : list[Account] = field(default_factory=list[Account])
    clients : list[People] = field(default_factory=list[People])


    def check_account(self,account):
        if any(existing_account is account for existing_account in self.accounts):
            print("account checked")
            return True
        print(f"account: {account.account} recused")
        return False
    
    def check_agency(self,account):
        if account.agency in self.agencies:
            print("agency checked")
            return True
        print(f"agency {account.agency} recused")
        return False
    
    def check_client(self,client):
        if any(existing_client is client for existing_client in self.clients):
            print(f"client checked")
            return True
        print(f"client named {client.name} recused")
        return False
    
    def check_client_account(self, client, account):
        if account is client.account:
            print(f"account : {account.account} is from {client.name}")
            return True
        print(f"account : {account.account} is not from {client.name}")
        return False
    
    def authenticate(self, client : People, account : Account):
        return self.check_account(account) and self.check_agency(account) and \
        self.check_client(client) and self.check_client_account(client, account)
    
