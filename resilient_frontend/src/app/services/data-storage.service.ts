import { Injectable } from '@angular/core';
import { RequestsService } from './requests.service';
import { User, Users } from '@shared/models/database-types';
import { Observable, map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataStorageService {

  constructor(
    private _requestsService: RequestsService,
  ) { }

  getUsers(): Observable<User[]> {
    return this._requestsService.getUsers().pipe(
      map((answer: Users) => {
        if (answer) {
          const usersArray: User[] = Object.values(answer.users);
          return usersArray.filter(user => {
            const role = user.role.toLowerCase();
            const active = user.active;
            return role !== 'admin' && role !== 'clinician' && role !== 'super_admin' && active;
          });
        }
        return [];
      })
    );
  }

  getReports(): Observable<any> {
    return this._requestsService.getReports().pipe(
      map((answer: any) => {
        if (answer) {
          return answer.reports;
        }
        return [];
      })
    );
  }

}
