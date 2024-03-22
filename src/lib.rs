extern crate difftastic;
extern crate pyo3;

use difftastic::{diff_file_content, option_types, print_diff_result, style};
// use pyo3::exceptions::*;
use pyo3::prelude::*;
// use pyo3::types::*;

#[pymodule]
#[pyo3(name = "difftasticpy")]
fn init_mod(_py: Python, m: &PyModule) -> PyResult<()> {
    // Functions
    #[pyfn(m)]
    #[pyo3(name = "foo")]
    fn to_object_rs<'a>(_py: Python<'a>, a: String, b: String, width: usize) -> PyResult<()> {
        let asd = diff_file_content(
            "console",
            a.as_bytes(),
            b.as_bytes(),
            1000,
            10_000_000,
            None,
        );
        print_diff_result(
            width,
            true,
            option_types::DisplayMode::SideBySideShowBoth,
            style::BackgroundColor::Dark,
            false,
            &asd,
        );
        Ok(())
    }

    Ok(())
}
