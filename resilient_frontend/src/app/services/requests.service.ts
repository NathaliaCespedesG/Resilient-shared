import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, ReplaySubject, map } from 'rxjs';
import { Users, Devices } from '../shared/models/database-types';
import { ICONS } from '../shared/constants/icons'
import { EnvService } from './env.service';
import { LocalStorageService } from './local-storage.service';

@Injectable({
  providedIn: 'root'
})
export class RequestsService {

  private icons = ICONS;
  private baseUrl: string;

  constructor(
    private http: HttpClient,
    private _envService: EnvService,
    private _localStorageService: LocalStorageService
  ) {
    this.baseUrl = this._envService.appConfig.apiUrl;
  }

  addParticipant(participantData: any): Observable<any> {
    const reqUrl = this.baseUrl + 'users/';

    return this.http.post<any>(reqUrl, participantData);
  }

  editParticipant(participantData: any): Observable<any> {
    const reqUrl = this.baseUrl + 'user/' + participantData.userId + '/';

    // if (Object.keys(participantData).length  2) {
    //   return this.http.put<any>(reqUrl, participantData);
    // }

    return this.http.patch<any>(reqUrl, participantData);
  }

  getUsers(): Observable<Users> {
    const usersFromStorage = this._localStorageService.getData('users');

    if (usersFromStorage) {
      return new Observable(observer => {
        observer.next(usersFromStorage);
        observer.complete();
      });
    }

    const usersUrl = this.baseUrl + 'users/';

    return this.http.get<Users>(usersUrl).pipe(
      map((answer: Users) => {
        let usersArray: Users = {users: [], loaded: false};

        if (answer) {
          usersArray = {
            users: Object.values(answer.users),
            loaded: true
          } ;
          usersArray.users = usersArray.users.filter(user => {
            const role = user.role.toLowerCase();
            const active = user.active;
            return role !== 'admin' && role !== 'clinician' && role !== 'super_admin' && active;
          });
        }

        this._localStorageService.setData('users', usersArray);
        return usersArray;

      })
    );
  }

  getDevices(): Observable<Devices> {
    const usersUrl = this.baseUrl + 'devices/';

    return this.http.get<Devices>(usersUrl);
  }

  getDevicesByUsername(username: string): Observable<any>{
    const devicesUrl = this.baseUrl + 'devices/?username=' + username;

    return this.http.get<any>(devicesUrl);
  }

  getDeviceSummaryByUsername(username: string, device_type: string): Observable<any>{
    const devicesUrl = this.baseUrl + this.icons[device_type].summaryUrl + '?username=' + username;

    return this.http.get<any>(devicesUrl);
  }

  saveWithingsCredentials(participantWithingsData: any): Observable<any> {
    const reqUrl = this.baseUrl + 'reports/withings-credentials/';

    return this.http.post<any>(reqUrl, participantWithingsData);
  }

  getReports(): Observable<any> {
    const reportsUrl = this.baseUrl + 'reports/';

    return this.http.get<any>(reportsUrl);
  }

  generateReport(username: string, reportType: string): Observable<Blob> {
    const reportsUrl = this.baseUrl + 'reports/generate/?username=' + username + '&report_type=' + reportType;

    return this.http.get<Blob>(reportsUrl, { responseType: 'blob' as 'json' });
  }


}
