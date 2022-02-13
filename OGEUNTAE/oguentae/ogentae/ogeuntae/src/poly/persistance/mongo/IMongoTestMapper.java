package poly.persistance.mongo;

public interface IMongoTestMapper {
	//test collection 생성 접속 확인용
	public boolean createCollection(String colNm) throws Exception;

}
