import './search-bar.css';

function SearchBar() {
    return (
        <div id='search-bar-wrapper'>
            <input
                type='text'
            />
            <i className="fa-solid fa-magnifying-glass"></i>
        </div>
    );
}

export default SearchBar;
